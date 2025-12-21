# 🎬 Coffeewood Entertainment

## 📖 Project Overview
**Coffeewood Entertainment** is a Django REST API backend for managing movies, user favorites, and comments with intelligent content moderation.

The inspiration for this project came from observing toxic comment sections on movie websites and social media. This platform aims to create a **safe, moderated environment** where users can discuss movies without encountering offensive content.

---

## ✨ Features

### 🔐 Authentication & User Management
- User registration with email validation
- JWT-based authentication (access & refresh tokens)
- Password recovery system with security questions
- User strike and blocking system

### 🎥 Movie Management
- Full CRUD operations (Admin only)
- Public movie browsing
- Search and filtering capabilities

### ⭐ Favorites System
- Add/remove movies from personal favorites
- View all favorited movies
- User-specific favorite lists

### 💬 Smart Comment Moderation
- **Automated content filtering** - banned words detection
- **Strike system** - users receive warnings for violations
- **Progressive blocking** - 3 strikes = account suspension
- Admin comment management and oversight

---

## 🛠️ Tech Stack

- **Backend:** Django 5.2.9, Django REST Framework
- **Authentication:** JWT (djangorestframework-simplejwt)
- **Database:** PostgreSQL 15
- **Testing:** pytest, pytest-django
- **Containerization:** Docker & Docker Compose

---

## 📋 Requirements

```
Python 3.11+
Django 5.2.9
djangorestframework 3.16.1
djangorestframework-simplejwt 5.5.1
psycopg[binary] 3.1.0+
dj-database-url 1.0.0+
pytest 7.0+
pytest-django 4.0+
```

---

## 🚀 Quick Start

### Option 1: Docker (Recommended)

1. **Clone the repository**
```bash
git clone https://github.com/Luka929-del/coffeewood_entertainment.git
cd coffeewood_entertainment
```

2. **Create environment file**
```bash
cp .env.example .env
# Edit .env with your credentials
```

3. **Build and start containers**
```bash
docker compose up --build
```

4. **Run migrations**
```bash
docker compose exec web python manage.py migrate
```

5. **Create admin user**
```bash
docker compose exec web python manage.py createsuperuser
```

6. **Access the application**
- API: http://localhost:8000
- Admin Panel: http://localhost:8000/admin

---

### Option 2: Local Development

1. **Clone and setup virtual environment**
```bash
git clone https://github.com/Luka929-del/coffeewood_entertainment.git
cd coffeewood_entertainment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure environment**
```bash
cp .env.example .env
# Edit .env with your database credentials
```

4. **Run migrations**
```bash
python manage.py migrate
```

5. **Create superuser**
```bash
python manage.py createsuperuser
```

6. **Start development server**
```bash
python manage.py runserver
```

---

## 🧪 Testing

### Run all tests
```bash
# Local
pytest -v

# Docker
docker compose exec web pytest -v
```

### Run specific test file
```bash
pytest movies/tests.py -v
pytest users/tests.py -v
```

### Test coverage
```bash
pytest --cov=. --cov-report=html
```

---

## 📚 API Documentation

### 🔑 Authentication

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/users/register/` | Register new user | ❌ |
| POST | `/api/token/` | Login (get JWT tokens) | ❌ |
| POST | `/api/token/refresh/` | Refresh access token | ❌ |
| GET/PUT | `/api/users/recovery/` | Manage recovery question | ✅ |
| POST | `/api/users/password-reset/` | Reset password | ❌ |

**Example: Register**
```bash
curl -X POST http://localhost:8000/api/users/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "username": "moviefan",
    "password": "SecurePass123"
  }'
```

**Example: Login**
```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "SecurePass123"
  }'
```

---

### 🎥 Movies

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/movies/` | List all movies | ❌ |
| POST | `/api/movies/` | Create movie | ✅ Admin |
| GET | `/api/movies/{id}/` | Get movie details | ❌ |
| PUT | `/api/movies/{id}/` | Update movie | ✅ Admin |
| DELETE | `/api/movies/{id}/` | Delete movie | ✅ Admin |

**Example: Create Movie (Admin only)**
```bash
curl -X POST http://localhost:8000/api/movies/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Inception",
    "description": "A mind-bending thriller",
    "release_year": 2010
  }'
```

---

### ⭐ Favorites

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/favorites/` | List user's favorites | ✅ |
| POST | `/api/favorites/` | Add to favorites | ✅ |
| DELETE | `/api/favorites/{id}/` | Remove from favorites | ✅ |

**Example: Add to Favorites**
```bash
curl -X POST http://localhost:8000/api/favorites/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"movie": 1}'
```

---

### 💬 Comments

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/movies/{movie_id}/comments/` | List comments | ❌ |
| POST | `/api/movies/{movie_id}/comments/` | Add comment | ✅ |
| DELETE | `/api/comments/{id}/delete/` | Delete comment | ✅ Owner/Admin |

**Example: Post Comment**
```bash
curl -X POST http://localhost:8000/api/movies/1/comments/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"text": "Amazing movie! Loved the plot twists."}'
```

---

## 🛡️ Content Moderation System

### How It Works

1. **Automated Filtering**
   - Comments are scanned for banned words in real-time
   - List includes offensive, hateful, and violent language

2. **Strike System**
   - ⚠️ **Strike 1:** Warning issued
   - ⚠️ **Strike 2:** Second warning
   - 🚫 **Strike 3:** Account blocked from commenting

3. **User Protection**
   - Blocked users cannot post new comments
   - Existing comments remain visible for context
   - Admins can review and manage user strikes

4. **Admin Controls**
   - View user strike counts in admin panel
   - Manually reset strikes if needed
   - Delete inappropriate comments
   - Monitor moderation activity

---

## 📁 Project Structure

```
coffeewood_entertainment/
├── coffeewood/              # Main project settings
│   ├── __init__.py
│   ├── settings.py         # Django configuration
│   ├── urls.py             # URL routing
│   ├── wsgi.py
│   └── asgi.py
├── movies/                  # Movies app
│   ├── migrations/
│   ├── models.py           # Movie, Favorite, Comment models
│   ├── views.py            # API views
│   ├── serializers.py      # DRF serializers
│   ├── permissions.py      # Custom permissions
│   ├── moderation.py       # Content moderation logic
│   ├── urls.py
│   ├── admin.py
│   └── tests.py
├── users/                   # Users app
│   ├── migrations/
│   ├── models.py           # Custom User model
│   ├── views.py            # Auth views
│   ├── serializers.py
│   ├── urls.py
│   └── tests.py
├── docker-compose.yml       # Docker configuration
├── Dockerfile
├── requirements.txt         # Python dependencies
├── pytest.ini              # Pytest configuration
├── .gitignore
├── .env.example            # Environment template
└── README.md
```

---

## 🔧 Environment Variables

Create a `.env` file in the root directory:

```env
# Django
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DATABASE_URL=postgresql://postgres:postgres@db:5432/coffeewood

# JWT (Optional - has defaults)
JWT_ACCESS_TOKEN_LIFETIME=60
JWT_REFRESH_TOKEN_LIFETIME=1440
```

---

## 🐳 Docker Commands

```bash
# Start services
docker compose up

# Start in background
docker compose up -d

# Stop services
docker compose down

# View logs
docker compose logs -f web

# Run migrations
docker compose exec web python manage.py migrate

# Create superuser
docker compose exec web python manage.py createsuperuser

# Run tests
docker compose exec web pytest -v

# Access Django shell
docker compose exec web python manage.py shell

# Rebuild containers
docker compose up --build
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👤 Author

**Luka**
- GitHub: [@Luka929-del](https://github.com/Luka929-del)

---

## 🙏 Acknowledgments

- Inspired by the need for safer online movie discussion communities
- Built with Django and Django REST Framework
- Special thanks to the open-source community

---

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check existing documentation
- Review API examples above

----

**⭐ If you find this project useful, please give it a star!**
