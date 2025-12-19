# Coffeewood Entertainment

## Project Overview
This is a Django-based backend project for managing movies, favorites, comments, and users with authentication.

## Features
- User registration, login, JWT authentication
- Movie CRUD (Admin only)
- Favorites and comments system
- Comment moderation, strike and block system
- Dockerized development environment
- PostgreSQL database

## Requirements
- Python 3.11
- Django 5.2.9
- djangorestframework
- djangorestframework_simplejwt
- psycopg[binary]
- dj-database-url
- pytest, pytest-django

## Setup
1. Clone the repository
2. Create `.env` file with DB credentials
3. Build and start docker containers:
```bash
docker compose up --build

Apply migrations: docker compose exec web python manage.py migrate

Run tests: docker compose exec web pytest -v

Project Structure:

coffeewood/
├── movies/
├── users/
├── manage.py
└── ...

