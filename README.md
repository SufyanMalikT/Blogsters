# 📝 Blogsters

**Blogsters** is a simple, full-stack blogging platform built with **Django**. It allows users to register, log in, create blog posts, and view posts from others. Ideal for learning how modern web applications are structured using Python and Django.

---

## 🚀 Features

- ✅ User authentication (signup, login, logout)
- 📝 Create, edit, and delete blog posts
- 📄 View blog posts by all users
- 🎨 Basic front-end with HTML, CSS, and JavaScript
- 🗄️ SQLite for local database storage
- 🌐 Deployment-ready with `Procfile`

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (default Django DB)
- **Deployment:** Heroku-ready (via `Procfile`)

---

## 📁 Project Structure

```bash
Blogsters/
├── accounts/          # Handles user registration and login
├── blog/              # Blog post models, views, templates
├── staticfiles/       # Static assets (CSS, JS)
├── db.sqlite3         # Local database
├── manage.py          # Django management script
├── requirements.txt   # Python dependencies
├── Procfile           # For deployment
└── .gitignore
