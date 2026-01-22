# 🎯 Visual Setup Guide - MediCare Pharmacy

## Step-by-Step Installation with Commands

### 📋 Prerequisites Checklist
```
☐ Python 3.8+ installed
☐ pip installed
☐ MariaDB/MySQL installed
☐ Terminal/Command Prompt access
☐ Text editor (VS Code, Sublime, etc.)
```

---

## 🚀 Installation Flow

```
┌─────────────────────────────────────────┐
│  Step 1: Install & Start MariaDB       │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  Step 2: Create Database & User        │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  Step 3: Setup Virtual Environment     │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  Step 4: Install Python Packages       │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  Step 5: Configure Database Settings   │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  Step 6: Run Database Migrations       │
└─────────────────────────────────────────┐
                    ↓
┌─────────────────────────────────────────┐
│  Step 7: Create Superuser Account      │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  Step 8: Add Sample Data (Optional)    │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  Step 9: Start Development Server      │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  ✅ Application Running!                │
│  🌐 http://127.0.0.1:8000/              │
└─────────────────────────────────────────┘
```

---

## 📝 Detailed Commands

### Step 1: Install MariaDB

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install mariadb-server mariadb-client -y
sudo systemctl start mariadb
sudo systemctl enable mariadb
sudo systemctl status mariadb  # Verify it's running
```

**macOS:**
```bash
brew install mariadb
brew services start mariadb
brew services list  # Verify it's running
```

**Windows:**
1. Download from: https://mariadb.org/download/
2. Run installer
3. Start MariaDB service from Services

---

### Step 2: Create Database

**Option A: Using SQL Script (Recommended)**
```bash
cd pharmacy_project
sudo mysql < setup_database.sql
```

**Option B: Manual Setup**
```bash
sudo mysql -u root -p

# In MySQL prompt:
CREATE DATABASE pharmacy_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'pharmacy_user'@'localhost' IDENTIFIED BY 'pharmacy123';
GRANT ALL PRIVILEGES ON pharmacy_db.* TO 'pharmacy_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

**Verify Database Creation:**
```bash
sudo mysql -u pharmacy_user -p pharmacy123 -e "SHOW DATABASES;"
```

Expected output:
```
+--------------------+
| Database           |
+--------------------+
| information_schema |
| pharmacy_db        |
+--------------------+
```

---

### Step 3: Setup Virtual Environment

```bash
# Navigate to project
cd pharmacy_project

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# Linux/Mac:
source venv/bin/activate

# Windows:
venv\Scripts\activate

# You should see (venv) in your terminal prompt
```

---

### Step 4: Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install all required packages
pip install -r requirements.txt

# Verify installation
pip list
```

Expected packages:
```
Django                 4.2.7
mysqlclient           2.2.0
Pillow                10.1.0
django-crispy-forms   2.1
crispy-bootstrap4     2.0
```

---

### Step 5: Configure Database

**Edit: `pharmacy_site/settings.py`**

Find this section (around line 50):
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pharmacy_db',
        'USER': 'pharmacy_user',
        'PASSWORD': 'your_password',  # ← CHANGE THIS
        'HOST': 'localhost',
        'PORT': '3306',
```

Update `PASSWORD` to match your database password:
```python
'PASSWORD': 'pharmacy123',  # or whatever you set
```

**Test database connection:**
```bash
python manage.py check --database default
```

Expected output:
```
System check identified no issues (0 silenced).
```

---

### Step 6: Run Migrations

```bash
# Create migration files
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# You should see output like:
# Operations to perform:
#   Apply all migrations: admin, auth, contenttypes, pharmacy, sessions
# Running migrations:
#   Applying pharmacy.0001_initial... OK
```

**Verify migrations:**
```bash
python manage.py showmigrations
```

---

### Step 7: Create Superuser

```bash
python manage.py createsuperuser

# Follow the prompts:
Username: admin
Email address: admin@example.com
Password: ******** (create a strong password)
Password (again): ********
Superuser created successfully.
```

**Important:** Remember these credentials for admin panel access!

---

### Step 8: Add Sample Data (Optional)

```bash
# Method 1: Using the script
python manage.py shell < populate_data.py

# Method 2: Manual via admin panel
# (Skip this and add via http://127.0.0.1:8000/admin/)
```

Expected output:
```
Creating sample medicines...
✓ Created: Paracetamol 500mg
✓ Created: Ibuprofen 200mg
...
Successfully created 20 medicines!
```

---

### Step 9: Start Server

```bash
# Start the development server
python manage.py runserver

# You should see:
# Watching for file changes with StatReloader
# Performing system checks...
# System check identified no issues (0 silenced).
# Django version 4.2.7, using settings 'pharmacy_site.settings'
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CONTROL-C.
```

---

## 🌐 Access the Application

### Open your browser and visit:

**Main Website:**
```
🏠 Home Page:        http://127.0.0.1:8000/
📦 Products:         http://127.0.0.1:8000/products/
🛒 Cart:             http://127.0.0.1:8000/cart/
📝 Register:         http://127.0.0.1:8000/register/
🔑 Login:            http://127.0.0.1:8000/login/
ℹ️  About:           http://127.0.0.1:8000/about/
📧 Contact:          http://127.0.0.1:8000/contact/
```

**Admin Panel:**
```
👨‍💼 Admin:            http://127.0.0.1:8000/admin/
   Username: admin (or what you created)
   Password: (what you set in step 7)
```

---

## ✅ Testing Checklist

### As Administrator:
```
☐ Login to admin panel
☐ Add a new medicine
☐ Upload an image
☐ View medicines list
☐ Edit medicine details
☐ Check inventory tracking
```

### As Customer:
```
☐ Register new account
☐ Login with credentials
☐ Browse products
☐ Search for medicine
☐ Add item to cart
☐ Update cart quantity
☐ Remove item from cart
☐ Proceed to checkout
☐ Place an order
☐ Confirm order
☐ View order history
☐ Logout
```

---

## 🐛 Common Issues & Solutions

### Issue 1: Can't connect to database
```
Error: django.db.utils.OperationalError: (2002, "Can't connect to MySQL server")

Solution:
1. Check if MariaDB is running:
   sudo systemctl status mariadb

2. Start MariaDB:
   sudo systemctl start mariadb

3. Verify credentials in settings.py
```

### Issue 2: mysqlclient won't install
```
Error: Failed building wheel for mysqlclient

Solution (Ubuntu):
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
pip install mysqlclient

Solution (macOS):
brew install mysql-client
export PATH="/usr/local/opt/mysql-client/bin:$PATH"
pip install mysqlclient
```

### Issue 3: Port already in use
```
Error: Error: That port is already in use.

Solution:
python manage.py runserver 8080
# Or any other port number
```

### Issue 4: Static files not loading
```
Solution:
python manage.py collectstatic --noinput
# Make sure DEBUG = True in settings.py for development
```

### Issue 5: Migration errors
```
Solution:
# Reset migrations
python manage.py migrate pharmacy zero
python manage.py migrate
```

---

## 📊 Project Health Check

Run these commands to verify everything is working:

```bash
# Check for errors
python manage.py check

# Verify database connection
python manage.py dbshell
# Then type: SHOW TABLES;

# List all migrations
python manage.py showmigrations

# Check installed apps
python manage.py shell
>>> from django.apps import apps
>>> apps.get_app_configs()
```

---

## 🎨 Customization Quick Guide

### Change Colors
Edit: `pharmacy/static/css/style.css`
```css
:root {
    --primary-color: #0d6efd;  /* Change this */
    --secondary-color: #6c757d;
}
```

### Change Logo Text
Edit: `pharmacy/templates/base.html`
```html
<span class="fs-4 fw-bold">MediCare Pharmacy</span>
<!-- Change to your pharmacy name -->
```

### Add New Medicine Fields
1. Edit: `pharmacy/models.py`
2. Run: `python manage.py makemigrations`
3. Run: `python manage.py migrate`

---

## 🔄 Daily Development Workflow

```bash
# 1. Activate virtual environment
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 2. Start server
python manage.py runserver

# 3. Make changes to files

# 4. If you changed models:
python manage.py makemigrations
python manage.py migrate

# 5. Test changes in browser

# 6. When done:
# Press Ctrl+C to stop server
deactivate  # Deactivate virtual environment
```

---

## 📚 Additional Resources

**Django Documentation:**
- Tutorial: https://docs.djangoproject.com/en/4.2/intro/tutorial01/
- Models: https://docs.djangoproject.com/en/4.2/topics/db/models/
- Views: https://docs.djangoproject.com/en/4.2/topics/http/views/

**MariaDB Documentation:**
- https://mariadb.com/kb/en/getting-started-with-mariadb/

**Bootstrap Documentation:**
- https://getbootstrap.com/docs/5.3/getting-started/introduction/

---

## 🎉 Success!

If you've completed all steps and can access the website, congratulations! 🎊

You now have a fully functional pharmacy website with:
- ✅ User authentication
- ✅ Product catalog
- ✅ Shopping cart
- ✅ Order management
- ✅ Inventory tracking
- ✅ Admin panel
- ✅ Beautiful UI

**Next Steps:**
1. Explore the admin panel
2. Add more medicines
3. Test all features
4. Customize as needed
5. Consider deployment (for production use)

---

**Need Help?** Check the README.md or QUICKSTART.md files!
