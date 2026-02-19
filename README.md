# 🎓 EduPortal — Student Management System

A production-ready, full-stack Student Portal with modern UI, JWT authentication, role-based access control, and comprehensive academic management features.

---

## 🚀 Quick Start

### Option A: Frontend Only (No Backend)
Simply open `frontend/index.html` in your browser — the demo runs with sample data immediately.

**Demo Credentials:**
| Role | Email | Password |
|------|-------|----------|
| Student | student1@portal.edu | Student@123 |
| Faculty | faculty@portal.edu | Faculty@123 |
| Admin | admin@portal.edu | Admin@123 |

---

### Option B: Full Stack Setup

#### Prerequisites
- Python 3.10+
- pip
- Node.js (optional, for live reload)
- PostgreSQL (optional, SQLite works for dev)

#### Backend Setup

```bash
# 1. Navigate to backend
cd student_portal/backend

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
cp .env.example .env
# Edit .env with your settings

# 5. Run migrations
python manage.py migrate

# 6. Create superuser
python manage.py createsuperuser

# 7. Populate sample data
python manage.py populate_sample_data

# 8. Start development server
python manage.py runserver
```

Backend runs at: `http://localhost:8000`
API Docs (Swagger): `http://localhost:8000/api/docs/`
Django Admin: `http://localhost:8000/admin/`

#### Frontend Setup

```bash
# Open with live server (VS Code extension recommended)
# Or use Python's simple server:
cd student_portal/frontend
python -m http.server 5500
```

Frontend runs at: `http://localhost:5500`

---

### Option C: Docker (Production)

```bash
# 1. Set environment variable
export SECRET_KEY="your-secret-key-50-chars-min"
export DB_PASSWORD="your-db-password"

# 2. Start all services
docker-compose up -d

# 3. View logs
docker-compose logs -f backend
```

---

## 📁 Project Structure

```
student_portal/
├── frontend/
│   └── index.html              # Complete SPA frontend
│
├── backend/
│   ├── config/
│   │   ├── settings.py         # Django settings
│   │   ├── urls.py             # Main URL config
│   │   └── wsgi.py
│   │
│   ├── apps/
│   │   ├── accounts/           # Auth, Users, Profiles
│   │   │   ├── models.py       # User, StudentProfile, FacultyProfile, OTP, LoginActivity, AuditLog
│   │   │   ├── serializers.py  # All auth serializers
│   │   │   ├── views.py        # Login, Register, Password Reset, Profile
│   │   │   ├── urls.py         # Auth URL routes
│   │   │   ├── permissions.py  # IsAdminUser, IsStudentUser, IsFacultyUser, etc.
│   │   │   ├── middleware.py   # Login activity tracking
│   │   │   └── management/commands/populate_sample_data.py
│   │   │
│   │   ├── courses/            # Departments, Courses, Enrollments
│   │   ├── attendance/         # Sessions, Records, Analytics
│   │   ├── results/            # Marks, Grades, PDF Memo
│   │   ├── assignments/        # Assignments, Submissions
│   │   ├── notices/            # Announcements, Events
│   │   ├── timetable/          # Weekly schedule
│   │   └── materials/          # Study materials, download center
│   │
│   ├── requirements.txt
│   ├── manage.py
│   ├── Dockerfile
│   └── .env.example
│
└── docker-compose.yml
```

---

## 🔌 API Reference

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/auth/login/` | Login with email/password → JWT tokens |
| POST | `/api/v1/auth/register/` | Create new user account |
| POST | `/api/v1/auth/logout/` | Invalidate refresh token |
| POST | `/api/v1/auth/token/refresh/` | Get new access token |
| POST | `/api/v1/auth/password/reset/request/` | Send OTP to email |
| POST | `/api/v1/auth/password/reset/confirm/` | Reset with OTP |
| POST | `/api/v1/auth/password/change/` | Change password |

### User / Profile
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET/PATCH | `/api/v1/auth/me/` | Current user info |
| POST | `/api/v1/auth/me/photo/` | Upload profile photo |
| GET/PATCH | `/api/v1/auth/me/student-profile/` | Student profile details |
| GET | `/api/v1/auth/me/login-activity/` | Login history |

### Courses
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/courses/` | All active courses |
| GET | `/api/v1/courses/my-enrollments/` | Student's enrolled courses |
| GET | `/api/v1/courses/admin/` | Admin course management |

### Attendance
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/attendance/summary/` | Subject-wise attendance % |
| GET | `/api/v1/attendance/course/<id>/` | Detailed records |
| POST | `/api/v1/attendance/admin/mark/` | Bulk mark attendance |

### Results
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/results/my/?semester=1` | Student marks |
| GET | `/api/v1/results/memo/download/` | PDF marks memo |
| POST | `/api/v1/results/admin/upload/` | Upload marks |

### Assignments
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/assignments/` | Student's assignments |
| POST | `/api/v1/assignments/<id>/submit/` | Submit assignment |
| GET | `/api/v1/assignments/submissions/` | Submission history |

### Timetable
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/timetable/my/` | Student's weekly timetable |

### Notices
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/notices/` | All notices (filtered by role) |
| POST | `/api/v1/notices/admin/` | Create notice (Admin/Faculty) |

### Materials
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/materials/` | All study materials |
| GET | `/api/v1/materials/<id>/` | Get material (increments download count) |
| POST | `/api/v1/materials/admin/` | Upload material |

---

## 🔐 Security Features

- **JWT Authentication** with short-lived access tokens (2h) and rotating refresh tokens (7 days)
- **Token blacklisting** on logout
- **Password hashing** via Django's PBKDF2 (bcrypt-compatible)
- **OTP verification** for password reset (10-minute expiry)
- **Login activity tracking** with IP address and user agent logging
- **Audit trail** for all CRUD operations
- **Role-based access control** (Student / Faculty / Admin)
- **CORS configuration** for API access control
- **Rate limiting** ready (via Redis)
- **HTTPS enforcement** in production

---

## 🎨 Frontend Features

- **Dual theme**: Dark/Light mode with persistent preference
- **Responsive**: Mobile, tablet, and desktop layouts
- **Role-based UI**: Different sidebar and pages for Student / Faculty / Admin
- **Real-time notifications** panel
- **Chart.js analytics**: Grades bar chart, attendance trend, department doughnut
- **CGPA ring** with animated SVG
- **Assignment management** with status tracking
- **Interactive timetable** grid
- **Toast notifications** for all actions
- **Glassmorphism + gradient accents**
- **Fonts**: Syne (display) + DM Sans (body) — distinctive, premium feel

---

## 🧩 Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML5, CSS3, Vanilla JS (ES6+), Chart.js |
| Backend | Django 4.2, Django REST Framework |
| Auth | djangorestframework-simplejwt (JWT) |
| Database | SQLite (dev) / PostgreSQL (prod) |
| Cache | Redis |
| PDF | ReportLab |
| Email | SMTP (Gmail/SendGrid) |
| Server | Gunicorn + Nginx |
| Container | Docker + Docker Compose |
| API Docs | drf-spectacular (Swagger/OpenAPI) |

---

## 🔄 Extending to React/Next.js

The backend is fully API-first. To integrate with React:

```javascript
// API client example
const API = 'http://localhost:8000/api/v1';
const token = localStorage.getItem('access_token');

const response = await fetch(`${API}/attendance/summary/`, {
  headers: { 'Authorization': `Bearer ${token}` }
});
const data = await response.json();
```

---

## 📧 Contact & Contributing

Built with ❤️ as a production-ready educational platform template.
Feel free to extend with: WebSocket notifications, mobile app API, LMS integration, payment gateway for fees.
