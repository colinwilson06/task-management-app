# Task Management App

A simple **fullstack Task Management App** built with **Vue.js** for frontend and **Python Flask** for backend, using **PostgreSQL** as database.  

---

## 💻 Tech Stack

- **Frontend:** Vue.js 3
- **Backend:** Python Flask
- **Database:** PostgreSQL
- **Authentication:** JWT (dummy login)
- **Other:** Axios, Flask-Cors, python-dotenv, psycopg2

---

## 📂 Project Structure

```bash
task-app/
├─ backend/
│ ├─ auth/ # Authentication routes
│ ├─ models/ # Database models
│ ├─ routes/ # Task CRUD routes
│ ├─ services/ # Business logic for tasks
│ ├─ app.py # Flask main app
│ ├─ config.py # Environment config
│ ├─ database.py # Database connection
│ └─ requirements.txt
├─ frontend/
│ ├─ components/ # Vue components (Login, TaskForm, TaskList, Toast)
│ ├─ views/ # Pages (Home.vue, Dashboard.vue)
│ ├─ router/ # Vue router
│ ├─ App.vue
│ └─ main.js
├─ .gitignore

```

---

## 🔧 Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL
- Git

---

## ⚙️ Setup & Run

### 1. Backend

1. Masuk ke folder backend:

```bash
cd backend
```

2. Buat virtual environment:

```bash
python -m venv venv
```

3. Aktifkan virtual environment:
   
   Windows:
   ```bash
   venv\Scripts\activate
   ```
   Linux / Mac:
   ```bash
   source venv/bin/activate
   ```

4. Install dependencies:
``` bash
pip install -r requirements.txt
```

5. Buat .env file di folder backend (contoh):
```bash
DB_HOST=localhost
DB_NAME=task_db
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_PORT=5432
SECRET_KEY=your_jwt_secret
```

6. Jalankan Backend:
```bash
python app.py
```
Backend akan berjalan di http://127.0.0.1:5000/


### 2. Frontend

1. Masuk ke folder frontend:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Jalankan frontend:
```bash
npm run serve
```
Frontend akan berjalan di http://localhost:8080/


---


🔑 Login

Username: admin
Password: admin123
Login ini menggunakan dummy JWT.


---


📝 Features

1. User login dengan JWT
   
2. CRUD Task:
   - Create Task (title, description, status)
   - Read Task List
   - Update Task
   - Delete Task
     
3. Task list:
   - Search tasks
   - Filter by status
   - Pagination
   - Drag & drop reorder

4. Frontend form validation
5. Light/Dark mode only on dashboard (not on login)


🎥 Video Demo

Demo Aplikasi: https://youtu.be/v0nxsx1K90k 

Arsitektur & Penjelasan Code: https://youtu.be/pPvmT-gQ3Dc
