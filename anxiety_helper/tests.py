"""
Unit tests for the Anxiety Helper API.

Run with:  python manage.py test
"""
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from accounts.models import User, Profile
from mood.models import MoodEntry


# ─── Helpers ──────────────────────────────────────────────────────────────────

def create_user(email="test@example.com", username="testuser", password="StrongPass123!"):
    return User.objects.create_user(username=username, email=email, password=password)


def get_tokens(client, email, password):
    url = reverse("login")
    resp = client.post(url, {"email": email, "password": password}, format="json")
    return resp.data.get("access"), resp.data.get("refresh")


# ─── Registration ─────────────────────────────────────────────────────────────

class UserRegistrationTests(APITestCase):
    url = reverse("register")

    def test_register_success(self):
        payload = {
            "username": "alice",
            "email": "alice@example.com",
            "password": "SecurePass99!",
            "password2": "SecurePass99!",
        }
        resp = self.client.post(self.url, payload, format="json")
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertIn("access", resp.data)
        self.assertIn("refresh", resp.data)
        self.assertEqual(resp.data["user"]["email"], "alice@example.com")

    def test_register_password_mismatch(self):
        payload = {
            "username": "bob",
            "email": "bob@example.com",
            "password": "SecurePass99!",
            "password2": "WrongPass!",
        }
        resp = self.client.post(self.url, payload, format="json")
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_duplicate_email(self):
        create_user(email="dup@example.com", username="dupuser")
        payload = {
            "username": "dupuser2",
            "email": "dup@example.com",
            "password": "SecurePass99!",
            "password2": "SecurePass99!",
        }
        resp = self.client.post(self.url, payload, format="json")
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_profile_auto_created_on_register(self):
        payload = {
            "username": "carol",
            "email": "carol@example.com",
            "password": "SecurePass99!",
            "password2": "SecurePass99!",
        }
        self.client.post(self.url, payload, format="json")
        user = User.objects.get(email="carol@example.com")
        self.assertTrue(hasattr(user, "profile"))
        self.assertIsInstance(user.profile, Profile)


# ─── Login ────────────────────────────────────────────────────────────────────

class UserLoginTests(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.url = reverse("login")

    def test_login_success(self):
        resp = self.client.post(
            self.url,
            {"email": "test@example.com", "password": "StrongPass123!"},
            format="json",
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertIn("access", resp.data)
        self.assertIn("refresh", resp.data)

    def test_login_wrong_password(self):
        resp = self.client.post(
            self.url,
            {"email": "test@example.com", "password": "WrongPassword!"},
            format="json",
        )
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_nonexistent_user(self):
        resp = self.client.post(
            self.url,
            {"email": "nobody@example.com", "password": "StrongPass123!"},
            format="json",
        )
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)


# ─── Profile ──────────────────────────────────────────────────────────────────

class ProfileTests(APITestCase):
    def setUp(self):
        self.user = create_user()
        access, _ = get_tokens(self.client, "test@example.com", "StrongPass123!")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")
        self.url = reverse("profile")

    def test_get_profile(self):
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data["email"], "test@example.com")

    def test_update_profile(self):
        resp = self.client.put(
            self.url,
            {"age": 28, "gender": "female", "anxiety_level": "moderate"},
            format="json",
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data["age"], 28)
        self.assertEqual(resp.data["gender"], "female")
        self.assertEqual(resp.data["anxiety_level"], "moderate")

    def test_profile_requires_auth(self):
        self.client.credentials()  # clear token
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)


# ─── Mood ─────────────────────────────────────────────────────────────────────

class MoodEntryTests(APITestCase):
    def setUp(self):
        self.user = create_user()
        access, _ = get_tokens(self.client, "test@example.com", "StrongPass123!")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")
        self.list_url = reverse("mood-list")

    def test_create_mood_entry(self):
        resp = self.client.post(
            self.list_url,
            {"mood": "anxious", "trigger": "work deadline", "notes": "Felt overwhelmed."},
            format="json",
        )
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(resp.data["mood"], "anxious")
        self.assertEqual(resp.data["trigger"], "work deadline")

    def test_list_mood_entries(self):
        MoodEntry.objects.create(user=self.user, mood="happy", trigger="", notes="")
        MoodEntry.objects.create(user=self.user, mood="neutral", trigger="", notes="")
        resp = self.client.get(self.list_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 2)

    def test_mood_entries_scoped_to_user(self):
        other_user = create_user(email="other@example.com", username="other")
        MoodEntry.objects.create(user=other_user, mood="sad", trigger="", notes="")
        MoodEntry.objects.create(user=self.user, mood="happy", trigger="", notes="")
        resp = self.client.get(self.list_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        # Should only see own entry
        self.assertEqual(len(resp.data), 1)
        self.assertEqual(resp.data[0]["mood"], "happy")

    def test_create_mood_invalid_choice(self):
        resp = self.client.post(
            self.list_url,
            {"mood": "ecstatic"},  # not a valid choice
            format="json",
        )
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_mood_requires_auth(self):
        self.client.credentials()
        resp = self.client.get(self.list_url)
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)


# ─── Token Refresh ────────────────────────────────────────────────────────────

class TokenRefreshTests(APITestCase):
    def setUp(self):
        create_user()
        _, self.refresh = get_tokens(self.client, "test@example.com", "StrongPass123!")

    def test_token_refresh(self):
        url = reverse("token_refresh")
        resp = self.client.post(url, {"refresh": self.refresh}, format="json")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertIn("access", resp.data)
