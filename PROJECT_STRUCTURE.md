# Pharmacy Website - Project Structure

## Directory Structure

```
pharmacy_project/
│
├── pharmacy_site/              # Main Django project folder
│   ├── __init__.py
│   ├── settings.py            # Project settings
│   ├── urls.py                # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
│
├── pharmacy/                   # Main application folder
│   ├── __init__.py
│   ├── admin.py               # Admin panel configuration
│   ├── apps.py
│   ├── models.py              # Database models (Medicine, Order, Cart)
│   ├── views.py               # View functions
│   ├── urls.py                # App URL configuration
│   ├── forms.py               # Forms for registration, login
│   ├── migrations/            # Database migrations
│   │   └── __init__.py
│   │
│   ├── templates/             # HTML templates
│   │   ├── base.html          # Base template with navbar
│   │   ├── home.html          # Home page with products
│   │   ├── about.html         # About page
│   │   ├── contact.html       # Contact page
│   │   ├── login.html         # Login page
│   │   ├── register.html      # Registration page
│   │   ├── logout.html        # Logout confirmation
│   │   ├── products.html      # Products listing
│   │   └── cart.html          # Shopping cart
│   │
│   └── static/                # Static files
│       ├── css/
│       │   ├── style.css      # Main stylesheet
│       │   ├── home.css       # Home page styles
│       │   ├── cart.css       # Cart page styles
│       │   └── forms.css      # Form styles
│       │
│       └── images/            # Logo and product images
│           └── logo.png
│
├── media/                     # User uploaded files
│   └── medicines/             # Medicine images
│
├── requirements.txt           # Python dependencies
├── manage.py                  # Django management script
└── README.md                  # Setup instructions
```

## Key Components

1. **Models** (models.py):
   - Medicine: Store medicine details, price, quantity
   - Cart: User cart items
   - Order: Completed orders

2. **Views** (views.py):
   - CRUD operations for medicines
   - Cart management
   - Order processing
   - Search functionality

3. **Templates**:
   - All HTML pages with Jinja2 templating
   - Responsive design with CSS

4. **Database**:
   - MariaDB for data persistence
   - Track inventory and sales
