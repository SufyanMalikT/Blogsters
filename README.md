# 📝 Blogsters

**Blogsters** is a full-stack blogging platform built with **Django**, featuring user authentication, post creation, and a clean UI. It is deployed using [Railway](https://railway.app/), making it easy to scale and manage.

---

## 🚀 Features

- ✅ User authentication (signup, login, logout)
- 📝 Create, edit, and delete blog posts
- 📄 View blog posts by all users
- 🎨 Simple, responsive frontend (HTML, CSS, JavaScript)
- 🗄️ SQLite (for development) – can be upgraded to PostgreSQL
- 🌐 Live deployment via Railway

---

## 🌐 Live Demo

🔗 [Visit the Live Site](https://blogsters.up.railway.app/)  
> Replace the above URL with your actual deployed app link.

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (local) / Railway-managed (e.g. PostgreSQL)
- **Deployment:** [Railway](https://railway.app/)

---

## 📁 Project Structure

```bash
Blogsters/
├── accounts/          # User authentication
├── blog/              # Blog logic and post management
├── staticfiles/       # CSS, JavaScript, static assets
├── db.sqlite3         # Local development database
├── manage.py          # Django management script
├── requirements.txt   # Dependencies
├── Procfile           # WSGI entry point for deployment
└── .gitignore
