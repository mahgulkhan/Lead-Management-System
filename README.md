# Lead Management System

A Flask-based lead management web application for Maison Consulting. Collects leads via a contact form and provides an admin dashboard for managing them.

## Features

- Contact form with lead submission
- Admin dashboard with CRUD operations (Create, Read, Update, Delete)
- Audit logging for all lead actions
- Responsive design
- SQLite database

## Tech Stack

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript

## Project Structure

```
Lead-Management-System/
├── static_files/          # CSS, JavaScript, images
├── web_pages/             # HTML templates
│   ├── admin_dashboard.html
│   ├── contact_form.html
│   ├── index.html
│   └── login.html
├── configurations.py      # Database setup & config
├── main_app.py            # Flask application (routes & APIs)
├── requirements.txt       # Python dependencies
├── setup_database.py      # Database initialization script
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/mahgulkhan/Lead-Management-System.git
cd Lead-Management-System
```

### 2. Set up virtual environment

```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
# OR
venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up the database

```bash
python setup_database.py
```

### 5. Run the application

```bash
python main_app.py
```

Access the app at `http://localhost:5000`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/submit-lead` | Submit a new lead |
| GET | `/api/get-leads` | Fetch all leads |
| GET | `/api/get-lead/<id>` | Fetch a specific lead |
| PUT | `/api/update-lead/<id>` | Update a lead |
| DELETE | `/api/delete-lead/<id>` | Delete a lead |
| POST | `/api/admin-login` | Admin authentication |
| GET | `/api/get-audit-logs` | Fetch audit logs |

## Default Admin Login

- **Username**: `admin`
- **Password**: `admin123`

*(Change these in `setup_database.py` before production)*

## Database Schema

### `leads` table
- `lead_id` (INTEGER PRIMARY KEY)
- `company_name` (TEXT)
- `contact_name` (TEXT)
- `email` (TEXT)
- `phone` (TEXT)
- `message` (TEXT)
- `source` (TEXT)
- `created_at` (DATETIME)

### `admin_users` table
- `admin_id` (INTEGER PRIMARY KEY)
- `username` (TEXT UNIQUE)
- `password_hash` (TEXT)

### `audit_log` table
- `log_id` (INTEGER PRIMARY KEY)
- `lead_id` (INTEGER)
- `admin_id` (INTEGER)
- `action` (TEXT)
- `timestamp` (DATETIME)

## Development Notes

- Debug mode is enabled (`debug=True`). Disable in production.
- Passwords are stored as plain text. **Hash them before production**.
- The app uses SQLite - suitable for development/low traffic only.
- For production, consider PostgreSQL/MySQL.

## Troubleshooting

### Database errors

```bash
rm lead_management.db
python setup_database.py
```

### Port already in use

```bash
python main_app.py --port=5001
```

## License

MIT License
