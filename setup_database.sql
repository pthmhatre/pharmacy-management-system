-- MediCare Pharmacy Database Setup Script
-- Run this script to set up the MariaDB database

-- Create database
CREATE DATABASE IF NOT EXISTS pharmacy_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Create user (change password for production)
CREATE USER IF NOT EXISTS 'pharmacy_user'@'localhost' IDENTIFIED BY 'pharmacy123';

-- Grant all privileges on pharmacy database
GRANT ALL PRIVILEGES ON pharmacy_db.* TO 'pharmacy_user'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;

-- Use the pharmacy database
USE pharmacy_db;

-- Show confirmation
SELECT 'Database pharmacy_db created successfully!' AS Status;
SELECT 'User pharmacy_user created with full privileges!' AS Status;

-- Display database information
SHOW DATABASES LIKE 'pharmacy_db';
SELECT user, host FROM mysql.user WHERE user = 'pharmacy_user';

-- Instructions
SELECT '========================================' AS '';
SELECT 'Database Setup Complete!' AS '';
SELECT '========================================' AS '';
SELECT 'Database Name: pharmacy_db' AS '';
SELECT 'Username: pharmacy_user' AS '';
SELECT 'Password: pharmacy123' AS '';
SELECT 'Host: localhost' AS '';
SELECT 'Port: 3306' AS '';
SELECT '' AS '';
SELECT 'Next Steps:' AS '';
SELECT '1. Update pharmacy_site/settings.py with these credentials' AS '';
SELECT '2. Run: python manage.py makemigrations' AS '';
SELECT '3. Run: python manage.py migrate' AS '';
SELECT '4. Run: python manage.py createsuperuser' AS '';
SELECT '5. Run: python manage.py runserver' AS '';
SELECT '========================================' AS '';
