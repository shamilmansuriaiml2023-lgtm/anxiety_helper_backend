# 🧘 Anxiety & Panic Helper — Django REST API

A production-ready backend for a mobile application that helps users manage anxiety and panic attacks.

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.12 |
| Framework | Django 5.x + Django REST Framework |
| Auth | JWT via `djangorestframework-simplejwt` |
| Database | SQLite (dev) / PostgreSQL (prod-ready) |
| CORS | `django-cors-headers` |
| Config | `python-dotenv` |

---

## 📦 Project Structure

```
anxiety_helper/
├── anxiety_helper/       # Core settings, URLs, WSGI
├── accounts/             # Custom User + Profile + Auth
├── mood/                 # Mood tracking
├── panic/                # Panic session recording
├── journal/              # Journal entries
├── emergency/            # Emergency contacts
├── affirmations/         # Daily affirmations + seed command
├── breathing/            # Breathing exercises
├── chatbot/              # Rule-based AI chatbot
├── dashboard/            # Aggregated dashboard
├── tests.py              # Unit tests
├── manage.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🚀 Setup Instructions

### 1. Clone and enter the project

```bash
git clone <your-repo-url>
cd anxiety_helper
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

```bash
cp .env.example .env
# Edit .env and set your SECRET_KEY
```

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Seed affirmations and breathing exercises

```bash
python manage.py seed_data
```

### 7. Create a superuser (for Django Admin)

```bash
python manage.py createsuperuser
```

### 8. Start the development server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

---

## 🧪 Running Tests

```bash
python manage.py test
```

---

## 🔑 Sample Credentials

After `createsuperuser`:

```
Email:    admin@example.com
Password: adminpass123
```

Admin panel: `http://127.0.0.1:8000/admin/`

---

## 📡 API Endpoints

### Authentication

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/auth/register/` | Register new user | No |
| POST | `/api/auth/login/` | Login and get tokens | No |
| POST | `/api/auth/token/refresh/` | Refresh access token | No |

### Profile

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/profile/` | Get current user's profile |
| PUT | `/api/profile/` | Update profile |

### Mood Tracker

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/moods/` | List all mood entries |
| POST | `/api/moods/` | Create a mood entry |
| GET | `/api/moods/{id}/` | Get a mood entry |
| PUT | `/api/moods/{id}/` | Update a mood entry |
| DELETE | `/api/moods/{id}/` | Delete a mood entry |

### Panic Sessions

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/panic-sessions/` | List all panic sessions |
| POST | `/api/panic-sessions/` | Record a panic session |
| GET | `/api/panic-sessions/{id}/` | Get a session |
| PUT | `/api/panic-sessions/{id}/` | Update a session |
| DELETE | `/api/panic-sessions/{id}/` | Delete a session |

### Journal

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/journal/` | List journal entries |
| POST | `/api/journal/` | Create a journal entry |
| GET | `/api/journal/{id}/` | Get an entry |
| PUT | `/api/journal/{id}/` | Update an entry |
| DELETE | `/api/journal/{id}/` | Delete an entry |

### Emergency Contacts

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/emergency-contacts/` | List contacts |
| POST | `/api/emergency-contacts/` | Add a contact |
| GET | `/api/emergency-contacts/{id}/` | Get a contact |
| PUT | `/api/emergency-contacts/{id}/` | Update a contact |
| DELETE | `/api/emergency-contacts/{id}/` | Delete a contact |

### Affirmations

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/affirmations/random/` | Get one random affirmation |

### Breathing Exercises

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/breathing-exercises/` | List all breathing exercises |
| GET | `/api/breathing-exercises/{id}/` | Get a specific exercise |

### Chatbot

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/chatbot/` | Send a message, get a supportive reply |

### Dashboard

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/dashboard/` | Get a summary of user's data |

---

## 📋 Sample API Requests & Responses

### Register

**Request**
```http
POST /api/auth/register/
Content-Type: application/json

{
  "username": "jane",
  "email": "jane@example.com",
  "password": "SecurePass99!",
  "password2": "SecurePass99!"
}
```

**Response** `201 Created`
```json
{
  "user": { "id": 1, "username": "jane", "email": "jane@example.com" },
  "access": "<jwt-access-token>",
  "refresh": "<jwt-refresh-token>"
}
```

---

### Login

**Request**
```http
POST /api/auth/login/
Content-Type: application/json

{
  "email": "jane@example.com",
  "password": "SecurePass99!"
}
```

**Response** `200 OK`
```json
{
  "user": { "id": 1, "username": "jane", "email": "jane@example.com" },
  "access": "<jwt-access-token>",
  "refresh": "<jwt-refresh-token>"
}
```

---

### Create Mood Entry

**Request**
```http
POST /api/moods/
Authorization: Bearer <access-token>
Content-Type: application/json

{
  "mood": "anxious",
  "trigger": "work presentation",
  "notes": "Felt my heart racing before the meeting."
}
```

**Response** `201 Created`
```json
{
  "id": 1,
  "mood": "anxious",
  "trigger": "work presentation",
  "notes": "Felt my heart racing before the meeting.",
  "created_at": "2025-06-01T10:30:00Z"
}
```

---

### Record Panic Session

**Request**
```http
POST /api/panic-sessions/
Authorization: Bearer <access-token>
Content-Type: application/json

{
  "intensity": 7,
  "trigger": "crowded mall",
  "duration_minutes": 15,
  "notes": "Happened at the food court."
}
```

**Response** `201 Created`
```json
{
  "id": 1,
  "intensity": 7,
  "trigger": "crowded mall",
  "duration_minutes": 15,
  "notes": "Happened at the food court.",
  "created_at": "2025-06-01T14:00:00Z"
}
```

---

### Chatbot

**Request**
```http
POST /api/chatbot/
Authorization: Bearer <access-token>
Content-Type: application/json

{
  "message": "I feel so anxious right now"
}
```

**Response** `200 OK`
```json
{
  "reply": "Take a slow, deep breath. You are safe right now. Anxiety is uncomfortable, but it is not dangerous. Try breathing in for 4 counts, holding for 4, and exhaling for 4. This feeling will pass — it always does."
}
```

---

### Dashboard

**Request**
```http
GET /api/dashboard/
Authorization: Bearer <access-token>
```

**Response** `200 OK`
```json
{
  "latest_mood": {
    "id": 3,
    "mood": "neutral",
    "trigger": "",
    "notes": "Feeling okay today.",
    "created_at": "2025-06-01T08:00:00Z"
  },
  "recent_journal_entries": [
    { "id": 2, "title": "Morning thoughts", "content": "...", "created_at": "...", "updated_at": "..." }
  ],
  "emergency_contacts_count": 2,
  "panic_sessions_count": 5
}
```

---

## 🔒 Security Notes

- All endpoints (except register and login) require a valid JWT `Bearer` token.
- Users can only access **their own** records — queryset filtering is applied at the view level.
- Rotate your `SECRET_KEY` before deploying to production.
- Set `DEBUG=False` and configure `ALLOWED_HOSTS` in production.
- Consider switching `CORS_ALLOW_ALL_ORIGINS = False` and whitelisting only your frontend domain in production.

---

## 📝 Mood Choices

| Value | Label |
|-------|-------|
| `very_happy` | Very Happy |
| `happy` | Happy |
| `neutral` | Neutral |
| `anxious` | Anxious |
| `sad` | Sad |
