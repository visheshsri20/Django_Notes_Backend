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
