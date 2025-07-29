# Django Notes API 📝

A RESTful API for a Notes application built with Django REST Framework, featuring JWT authentication and complete CRUD operations.

## 🚀 Features

- **User Authentication**: Registration and JWT-based login
- **CRUD Operations**: Create, Read, Update, Delete notes
- **Security**: JWT token authentication for protected endpoints
- **User Isolation**: Users can only access their own notes
- **RESTful Design**: Clean and intuitive API endpoints

## 🛠️ Technologies Used

- **Backend**: Django, Django REST Framework
- **Authentication**: JWT (JSON Web Tokens)
- **Database**: SQLite (development)
- **Python**: 3.11+

## 📋 API Endpoints

### Authentication
```
POST /api/user/register/     # User registration
POST /api/token/             # Get JWT tokens
POST /api/token/refresh/     # Refresh JWT token
```

### Notes (Authenticated)
```
GET    /api/notes/                 # List all notes a user has saved till now
POST   /api/notes/                 # Create new note (Requires an access token)
PUT    /api/notes/update/{id}/     # Update existing note (Requires an access token and a private key)
PATCH  /api/notes/update/{id}/     # Partially update note (Requires an access token and a private key)
DELETE /api/notes/delete/{id}/     # Delete note (Requires an access token and a private key)
```

## 🔧 Installation & Setup

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/django-notes-api.git
   cd django-notes-api
   ```

2. **Create virtual environment**
   ```bash
   python -m venv env
   ```

3. **Activate virtual environment**
   ```bash
   # Windows
   env\Scripts\activate
   
   # macOS/Linux
   source env/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations**
   ```bash
   cd backend
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Start development server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`

## 🧪 Testing the API

### 1. Register a User
```bash
curl -X POST http://127.0.0.1:8000/api/user/register/ \
-H "Content-Type: application/json" \
-d '{"username": "testuser", "password": "testpass123"}'
```

### 2. Get JWT Token
```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
-H "Content-Type: application/json" \
-d '{"username": "testuser", "password": "testpass123"}'
```

### 3. Create a Note
```bash
curl -X POST http://127.0.0.1:8000/api/notes/ \
-H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
-H "Content-Type: application/json" \
-d '{"title": "My Note", "content": "Note content here"}'
```

### 4. List Notes
```bash
curl -X GET http://127.0.0.1:8000/api/notes/ \
-H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## 📁 Project Structure

```
django-notes-api/
├── backend/
│   ├── manage.py
│   ├── backend/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   └── api/
│       ├── models.py
│       ├── serializer.py
│       ├── views.py
│       ├── urls.py
│       └── ...
├── env/                    # Virtual environment (not in repo)
├── requirements.txt
├── .gitignore
└── README.md
```

## 🔐 Security Features

- JWT token-based authentication
- Password hashing using Django's built-in security
- User isolation (users can only access their own notes)
- Protected endpoints requiring authentication
