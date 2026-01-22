# Quick Start Guide - MediCare Pharmacy

## Fastest Way to Get Started (5 Minutes)

### 1. Install MariaDB and Create Database
```bash
# Ubuntu/Debian
sudo apt install mariadb-server -y
sudo systemctl start mariadb

# Create database
sudo mysql -e "CREATE DATABASE pharmacy_db; CREATE USER 'pharmacy_user'@'localhost' IDENTIFIED BY 'pharmacy123'; GRANT ALL PRIVILEGES ON pharmacy_db.* TO 'pharmacy_user'@'localhost'; FLUSH PRIVILEGES;"
```

### 2. Setup Virtual Environment
```bash
cd pharmacy_project
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Update Database Password
Edit `pharmacy_site/settings.py`, line ~50:
```python
'PASSWORD': 'pharmacy123',  # Match the password from step 1
```

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Admin User
```bash
python manage.py createsuperuser
# Username: admin
# Email: admin@example.com
# Password: admin123 (or your choice)
```

### 7. Create Directories
```bash
mkdir -p media/medicines
```

### 8. Start Server
```bash
python manage.py runserver
```

### 9. Access Application
- **Website**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## First Steps After Starting

1. **Login to Admin Panel**:
   - Go to http://127.0.0.1:8000/admin/
   - Login with admin credentials

2. **Add Sample Medicines**:
   - Click "Medicines" → "Add Medicine"
   - Fill in:
     * Name: Paracetamol 500mg
     * Description: Pain relief medication
     * Manufacturer: PharmaCorp
     * Price: 5.99
     * Quantity Available: 100
     * Category: Pain Relief
   - Click "Save"
   - Add a few more medicines

3. **Test the Website**:
   - Go to http://127.0.0.1:8000/
   - Click "Register" and create a user account
   - Browse products
   - Add items to cart
   - Place an order

## Common Commands

```bash
# Start server
python manage.py runserver

# Create admin user
python manage.py createsuperuser

# Reset database (WARNING: Deletes all data)
python manage.py flush

# Access Django shell
python manage.py shell

# Check for issues
python manage.py check
```

## Troubleshooting

### Can't connect to database?
```bash
# Check if MariaDB is running
sudo systemctl status mariadb

# Restart MariaDB
sudo systemctl restart mariadb
```

### Module not found error?
```bash
# Make sure virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Static files not loading?
```bash
python manage.py collectstatic --noinput
```

## Next Steps

- Read full README.md for detailed information
- Explore admin panel features
- Customize templates and styles
- Add more sample data
- Test all features

## File Locations Reference

```
pharmacy_project/
├── manage.py              ← Main management script
├── requirements.txt       ← Dependencies
├── README.md             ← Full documentation
├── pharmacy_site/
│   └── settings.py       ← Database configuration HERE
└── pharmacy/
    ├── models.py         ← Database models
    ├── views.py          ← Business logic
    ├── templates/        ← HTML files
    └── static/css/       ← Stylesheets
```

## Default Credentials (Change in Production!)

- **Database User**: pharmacy_user
- **Database Password**: pharmacy123
- **Admin User**: admin (you create this)
- **Admin Password**: (you choose this)

---

**Need Help?** Check README.md for detailed instructions and troubleshooting.
