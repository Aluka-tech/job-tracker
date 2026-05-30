# Trackly — Job Application Tracker

A full-stack web application for tracking job applications, built with Django and vanilla JavaScript.

🔗 **Live Demo:** https://job-tracker-aje3.onrender.com

---

## Features

- User authentication (register, login, logout)
- Add, edit, and delete job applications
- Track application status: Applied → Interview → Offer → Rejected
- Dashboard with live stats and recent applications
- Live search and status filtering
- Toast notifications on save
- Fully responsive — works on mobile and desktop

---

## Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Vanilla JavaScript
- **Database:** PostgreSQL (production), SQLite (development)
- **Deployment:** Render
- **Version Control:** Git & GitHub

---

## Getting Started (Local Setup)

1. Clone the repository
```bash
   git clone https://github.com/Aluka-tech/job-tracker.git
   cd job-tracker
```

2. Install dependencies
```bash
   pip install -r requirements.txt
```

3. Run migrations
```bash
   python manage.py migrate
```

4. Start the development server
```bash
   python manage.py runserver
```

5. Visit `http://127.0.0.1:8000`

---

Built by [Chibuzor Aluka](https://github.com/Aluka-tech)