# MediCare Pharmacy - Django Web Application

A comprehensive online pharmacy management system built with Django and MariaDB.

## Features

- **User Authentication**: Register, login, logout functionality
- **Product Management**: Browse medicines with detailed information
- **Shopping Cart**: Add/remove items, update quantities
- **Order Management**: Place orders, track status, confirm orders
- **Inventory Tracking**: Real-time stock availability, sold quantity tracking
- **Search Functionality**: Live search for medicines
- **Responsive Design**: Mobile-friendly interface
- **Order Notifications**: Pop-up notifications on order placement
- **Admin Panel**: Full CRUD operations for medicines and orders

## Project Structure

```
pharmacy_project/
├── pharmacy_site/          # Main project settings
│   ├── settings.py        # Database and app configuration
│   ├── urls.py            # URL routing
│   ├── wsgi.py
│   └── asgi.py
├── pharmacy/              # Main application
│   ├── models.py          # Database models (Medicine, Cart, Order)
│   ├── views.py           # View functions
│   ├── urls.py            # App URLs
│   ├── forms.py           # Form classes
│   ├── admin.py           # Admin configuration
│   ├── context_processors.py  # Custom context processors
│   ├── templates/         # HTML templates
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── products.html
│   │   ├── cart.html
│   │   ├── checkout.html
│   │   ├── order_detail.html
│   │   ├── my_orders.html
│   │   ├── register.html
│   │   ├── login.html
│   │   ├── logout.html
│   │   ├── about.html
│   │   └── contact.html
│   └── static/           # CSS and images
│       └── css/
│           ├── style.css
│           ├── home.css
│           ├── cart.css
│           └── forms.css
├── media/                # Uploaded files (medicine images)
├── manage.py             # Django management script
└── requirements.txt      # Python dependencies
```

## Prerequisites

- Python 3.8 or higher
- MariaDB 10.5 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Installation Steps

### Step 1: Install MariaDB

**On Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install mariadb-server mariadb-client
sudo systemctl start mariadb
sudo systemctl enable mariadb
sudo mysql_secure_installation
```

**On Windows:**
Download and install from: https://mariadb.org/download/

**On macOS:**
```bash
brew install mariadb
brew services start mariadb
```

### Step 2: Create Database

```bash
# Login to MariaDB
sudo mysql -u root -p

# Create database
CREATE DATABASE pharmacy_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# Create user (optional but recommended)
CREATE USER 'pharmacy_user'@'localhost' IDENTIFIED BY 'your_strong_password';

# Grant privileges
GRANT ALL PRIVILEGES ON pharmacy_db.* TO 'pharmacy_user'@'localhost';

# Flush privileges
FLUSH PRIVILEGES;

# Exit
EXIT;
```

### Step 3: Set Up Virtual Environment

```bash
# Navigate to project directory
cd pharmacy_project

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### Step 4: Install Python Dependencies

```bash
# Install required packages
pip install --upgrade pip
pip install -r requirements.txt
```

**Note:** If you encounter errors installing `mysqlclient`, you may need to install system dependencies:

**Ubuntu/Debian:**
```bash
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
```

**macOS:**
```bash
brew install mysql-client
export PATH="/usr/local/opt/mysql-client/bin:$PATH"
```

**Windows:**
Download and install Microsoft Visual C++ 14.0 or greater from:
https://visualstudio.microsoft.com/visual-cpp-build-tools/

### Step 5: Configure Database Settings

Edit `pharmacy_site/settings.py` and update the database configuration:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pharmacy_db',
        'USER': 'pharmacy_user',  # or 'root'
        'PASSWORD': 'your_strong_password',  # your database password
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}
```

### Step 6: Run Migrations

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate
```

### Step 7: Create Superuser (Admin Account)

```bash
python manage.py createsuperuser

# Follow the prompts to create admin credentials:
# Username: admin
# Email: admin@example.com
# Password: (create a strong password)
```

### Step 8: Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### Step 9: Create Media Directories

```bash
mkdir -p media/medicines
```

### Step 10: Run Development Server

```bash
python manage.py runserver
```

The application will be available at: http://127.0.0.1:8000/

## Accessing the Application

### User Interface
- **Home Page**: http://127.0.0.1:8000/
- **Products**: http://127.0.0.1:8000/products/
- **Register**: http://127.0.0.1:8000/register/
- **Login**: http://127.0.0.1:8000/login/
- **Cart**: http://127.0.0.1:8000/cart/ (requires login)
- **About**: http://127.0.0.1:8000/about/
- **Contact**: http://127.0.0.1:8000/contact/

### Admin Panel
- **URL**: http://127.0.0.1:8000/admin/
- **Login**: Use the superuser credentials created in Step 7

## Adding Sample Data

### Method 1: Via Admin Panel

1. Login to admin panel: http://127.0.0.1:8000/admin/
2. Click on "Medicines"
3. Click "Add Medicine"
4. Fill in the details:
   - Name: e.g., "Paracetamol 500mg"
   - Description: e.g., "Pain relief and fever reducer"
   - Manufacturer: e.g., "PharmaCorp"
   - Price: e.g., 5.99
   - Quantity Available: e.g., 100
   - Category: e.g., "Pain Relief"
   - Upload image (optional)
5. Click "Save"

### Method 2: Via Django Shell

```bash
python manage.py shell
```

```python
from pharmacy.models import Medicine

# Create sample medicines
Medicine.objects.create(
    name="Paracetamol 500mg",
    description="Effective pain relief and fever reducer",
    manufacturer="PharmaCorp",
    price=5.99,
    quantity_available=100,
    category="Pain Relief"
)

Medicine.objects.create(
    name="Amoxicillin 250mg",
    description="Antibiotic for bacterial infections",
    manufacturer="MediLabs",
    price=12.99,
    quantity_available=50,
    category="Antibiotics",
    prescription_required=True
)

Medicine.objects.create(
    name="Vitamin C 1000mg",
    description="Immune system support supplement",
    manufacturer="HealthPlus",
    price=8.99,
    quantity_available=200,
    category="Vitamins"
)

# Verify
Medicine.objects.all()
```

## Usage Guide

### For Customers

1. **Registration**:
   - Click "Register" in navigation
   - Fill in the registration form
   - Click "Register" button
   - Login with credentials

2. **Browsing Products**:
   - View featured products on home page
   - Click "Products" to see all medicines
   - Use search bar to find specific medicines
   - Filter by category

3. **Adding to Cart**:
   - Select quantity
   - Click "Add to Cart" button
   - View cart by clicking cart icon

4. **Placing Order**:
   - Review items in cart
   - Update quantities if needed
   - Click "Proceed to Checkout"
   - Enter shipping address and contact number
   - Click "Place Order"
   - Confirm order on order detail page

5. **Tracking Orders**:
   - Click "Orders" in navigation
   - View all your orders
   - Click on order to see details

### For Administrators

1. **Login to Admin Panel**:
   - Go to http://127.0.0.1:8000/admin/
   - Enter superuser credentials

2. **Managing Medicines**:
   - Add new medicines with details and images
   - Update stock quantities
   - Edit prices and descriptions
   - View sold quantities

3. **Managing Orders**:
   - View all orders
   - Update order status
   - View order details and items

4. **Managing Users**:
   - View registered users
   - Manage user permissions

## CRUD Operations

The application implements full CRUD operations:

### Create
- Add new medicines (Admin)
- Register new users
- Create orders
- Add items to cart

### Read
- View all medicines
- Search medicines
- View cart items
- View order history
- Check inventory levels

### Update
- Update cart quantities
- Modify medicine details (Admin)
- Change order status (Admin)
- Update user profile

### Delete
- Remove items from cart
- Delete medicines (Admin)
- Cancel orders (Admin)

## Database Schema

### Medicine Table
- id (Primary Key)
- name
- description
- manufacturer
- price
- quantity_available
- quantity_sold
- image
- prescription_required
- category
- created_at
- updated_at

### Cart Table
- id (Primary Key)
- user_id (Foreign Key)
- medicine_id (Foreign Key)
- quantity
- added_at

### Order Table
- id (Primary Key)
- user_id (Foreign Key)
- order_number
- total_amount
- status
- shipping_address
- contact_number
- created_at
- updated_at
- confirmed_at

### OrderItem Table
- id (Primary Key)
- order_id (Foreign Key)
- medicine_id (Foreign Key)
- quantity
- price

## Features in Detail

### Inventory Management
- Real-time stock tracking
- Automatic quantity reduction on order
- Sold quantity tracking
- Stock availability indicators

### Search Functionality
- Live search with AJAX
- Search by name, manufacturer, description
- Category filtering
- Availability status

### Order System
- Shopping cart with quantity controls
- Order placement with address
- Order confirmation feature
- Order status tracking
- Order history

### Notifications
- Success messages for cart actions
- Order placement alerts
- Stock availability warnings
- Error notifications

## Troubleshooting

### Database Connection Error
```
django.db.utils.OperationalError: (2002, "Can't connect to MySQL server")
```
**Solution**: Ensure MariaDB is running and credentials are correct in settings.py

### Migration Issues
```bash
# Reset migrations
python manage.py migrate pharmacy zero
python manage.py migrate
```

### Static Files Not Loading
```bash
python manage.py collectstatic --clear
python manage.py collectstatic --noinput
```

### Port Already in Use
```bash
# Run on different port
python manage.py runserver 8080
```

## Development Tips

### Running Tests
```bash
python manage.py test
```

### Creating Database Backup
```bash
mysqldump -u pharmacy_user -p pharmacy_db > backup.sql
```

### Restoring Database
```bash
mysql -u pharmacy_user -p pharmacy_db < backup.sql
```

### Checking Database
```bash
python manage.py dbshell
```

## Security Considerations

1. Change `SECRET_KEY` in settings.py for production
2. Set `DEBUG = False` in production
3. Use environment variables for sensitive data
4. Enable HTTPS in production
5. Use strong passwords for database and admin

## Future Enhancements

- Payment gateway integration
- Email notifications
- SMS alerts
- Prescription upload feature
- Medicine reviews and ratings
- Advanced search filters
- Order tracking with delivery status
- Bulk order discounts
- Wishlist functionality
- Medicine recommendations

## Support

For issues or questions:
- Check the troubleshooting section
- Review Django documentation: https://docs.djangoproject.com/
- Check MariaDB documentation: https://mariadb.com/kb/en/

## License

This project is created for educational purposes.

## Credits

Built with:
- Django 4.2.7
- Bootstrap 5.3
- Font Awesome 6.4
- jQuery 3.6

---

**Author**: Django Pharmacy Team
**Version**: 1.0.0
**Last Updated**: 2024
