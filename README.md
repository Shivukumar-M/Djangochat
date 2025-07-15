
# DjangoChat

A real‑time chat application built with Django, Django Channels, WebSockets, and React (or plain JS), enabling instant messaging, friend requests, group chats, and real‑time notifications.

---

## 🚀 Features

- **User Authentication**: Secure signup, login, logout
- **Friend Management**: Send, accept, reject, and remove friend requests
- **One-to-One & Group Chats**:
  - Real-time messaging via WebSockets
  - Message storage in the database
- **Group Management**:
  - Create groups, send/accept join requests
  - Add/remove members (admins only)
  - Real-time group updates across clients
- **Search Functionality**: Locate users or groups
- **Notifications**: Immediate in-app notifications for friend requests and group changes
- **Responsive UI**: Optimized for mobile and desktop

---

## 🧰 Technologies Used

- **Backend**:
  - Django
  - Django Channels
  - Daphne
  - WebSockets
  - (Optional) REST framework if you use Django Rest Framework
  - Channels Layer Redis (development uses in-memory or SQLite)
- **Frontend**:
  - React (if present): React Router, Axios, WebSockets, Toastify, SweetAlert2
  - Or Plain JavaScript, HTML, CSS

---

## 📦 Installation & Local Setup

### 🤖 Prerequisites

- Python 3.8+
- Node.js & npm (if frontend is React)
- Redis (recommended for production; in-memory layer OK for dev)

### 📥 Clone the repo

```bash
git clone https://github.com/Shivukumar-M/Djangochat.git
cd Djangochat
```

### 🐍 Backend Setup

```bash
python3 -m venv venv
source venv/bin/activate      # (or venv\Scripts\activate on Windows)
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Your Django backend server should now run on `http://127.0.0.1:8000`

### ⚛️ Frontend Setup (if applicable)

```bash
cd chat_react              # or your frontend folder
npm install
npm start
```

Frontend should now run on `http://127.0.0.1:3000`

> ⚠️ Use `127.0.0.1:3000` instead of `localhost:3000` to avoid cookie/CORS issues when talking to the backend.

---

## 🛠️ Configuration

- **Channels Layer**: Switch to Redis for production by updating `CHANNEL_LAYERS` in `settings.py`.
- **Database**: Defaults to SQLite; switch to PostgreSQL/MySQL in production.
- **Environment Variables**: Store sensitive values (`SECRET_KEY`, DB credentials, etc.) using `.env` or your CI/CD secrets.

---

## 📸 Screenshots / Demo




After new message sent by code 

---




