"""
Sample Data Population Script for MediCare Pharmacy

Run this script after migrations to populate the database with sample medicines.

Usage:
    python manage.py shell < populate_data.py

Or copy and paste the code into Django shell:
    python manage.py shell
"""

from pharmacy.models import Medicine

# Sample medicines data
medicines_data = [
    {
        'name': 'Paracetamol 500mg',
        'description': 'Effective pain relief and fever reducer. Safe for adults and children over 12.',
        'manufacturer': 'PharmaCorp',
        'price': 5.99,
        'quantity_available': 100,
        'category': 'Pain Relief',
        'prescription_required': False
    },
    {
        'name': 'Ibuprofen 200mg',
        'description': 'Anti-inflammatory pain reliever. Reduces pain, fever, and inflammation.',
        'manufacturer': 'HealthPlus',
        'price': 7.99,
        'quantity_available': 80,
        'category': 'Pain Relief',
        'prescription_required': False
    },
    {
        'name': 'Amoxicillin 250mg',
        'description': 'Broad-spectrum antibiotic for bacterial infections. Take as prescribed.',
        'manufacturer': 'MediLabs',
        'price': 12.99,
        'quantity_available': 50,
        'category': 'Antibiotics',
        'prescription_required': True
    },
    {
        'name': 'Azithromycin 500mg',
        'description': 'Antibiotic medication for respiratory and other bacterial infections.',
        'manufacturer': 'BioPharm',
        'price': 15.99,
        'quantity_available': 40,
        'category': 'Antibiotics',
        'prescription_required': True
    },
    {
        'name': 'Vitamin C 1000mg',
        'description': 'Essential vitamin for immune system support. One tablet daily.',
        'manufacturer': 'HealthPlus',
        'price': 8.99,
        'quantity_available': 200,
        'category': 'Vitamins',
        'prescription_required': False
    },
    {
        'name': 'Vitamin D3 2000 IU',
        'description': 'Supports bone health and immune function. Helps calcium absorption.',
        'manufacturer': 'WellnessLab',
        'price': 11.99,
        'quantity_available': 150,
        'category': 'Vitamins',
        'prescription_required': False
    },
    {
        'name': 'Multivitamin Complex',
        'description': 'Complete daily multivitamin with essential minerals and nutrients.',
        'manufacturer': 'HealthPlus',
        'price': 14.99,
        'quantity_available': 120,
        'category': 'Vitamins',
        'prescription_required': False
    },
    {
        'name': 'Aspirin 100mg',
        'description': 'Low-dose aspirin for heart health and blood thinning. Doctor recommended.',
        'manufacturer': 'CardioMed',
        'price': 6.99,
        'quantity_available': 90,
        'category': 'Cardiovascular',
        'prescription_required': False
    },
    {
        'name': 'Omeprazole 20mg',
        'description': 'Reduces stomach acid production. Treats heartburn and acid reflux.',
        'manufacturer': 'GastroPharm',
        'price': 9.99,
        'quantity_available': 70,
        'category': 'Digestive Health',
        'prescription_required': False
    },
    {
        'name': 'Cetirizine 10mg',
        'description': 'Antihistamine for allergy relief. Non-drowsy formula for daily use.',
        'manufacturer': 'AllergyFree',
        'price': 8.49,
        'quantity_available': 110,
        'category': 'Allergy',
        'prescription_required': False
    },
    {
        'name': 'Loratadine 10mg',
        'description': '24-hour allergy relief. Effective against seasonal and year-round allergies.',
        'manufacturer': 'AllergyFree',
        'price': 7.99,
        'quantity_available': 95,
        'category': 'Allergy',
        'prescription_required': False
    },
    {
        'name': 'Metformin 500mg',
        'description': 'Diabetes medication to control blood sugar levels. Extended release formula.',
        'manufacturer': 'DiabeteCare',
        'price': 13.99,
        'quantity_available': 60,
        'category': 'Diabetes',
        'prescription_required': True
    },
    {
        'name': 'Insulin Glargine 100 units/ml',
        'description': 'Long-acting insulin for diabetes management. Refrigerate after opening.',
        'manufacturer': 'DiabeteCare',
        'price': 45.99,
        'quantity_available': 25,
        'category': 'Diabetes',
        'prescription_required': True
    },
    {
        'name': 'First Aid Kit - Complete',
        'description': 'Comprehensive first aid kit with bandages, antiseptics, and medical supplies.',
        'manufacturer': 'SafetyFirst',
        'price': 29.99,
        'quantity_available': 35,
        'category': 'First Aid',
        'prescription_required': False
    },
    {
        'name': 'Digital Thermometer',
        'description': 'Fast and accurate digital thermometer. Oral, rectal, and underarm use.',
        'manufacturer': 'MedTech',
        'price': 12.99,
        'quantity_available': 50,
        'category': 'Medical Devices',
        'prescription_required': False
    },
    {
        'name': 'Blood Pressure Monitor',
        'description': 'Automatic digital blood pressure monitor. Large LCD display with memory.',
        'manufacturer': 'CardioMed',
        'price': 39.99,
        'quantity_available': 30,
        'category': 'Medical Devices',
        'prescription_required': False
    },
    {
        'name': 'Cough Syrup - Honey & Lemon',
        'description': 'Natural cough suppressant with honey and lemon. Soothes throat irritation.',
        'manufacturer': 'NatureCure',
        'price': 9.99,
        'quantity_available': 75,
        'category': 'Cold & Flu',
        'prescription_required': False
    },
    {
        'name': 'Antiseptic Hand Sanitizer',
        'description': '70% alcohol-based hand sanitizer. Kills 99.9% of germs. 500ml bottle.',
        'manufacturer': 'SafetyFirst',
        'price': 6.99,
        'quantity_available': 200,
        'category': 'Hygiene',
        'prescription_required': False
    },
    {
        'name': 'Calcium + Vitamin D Tablets',
        'description': 'Supports bone health and strength. Combination of calcium and vitamin D.',
        'manufacturer': 'BoneHealth',
        'price': 13.49,
        'quantity_available': 85,
        'category': 'Vitamins',
        'prescription_required': False
    },
    {
        'name': 'Probiotic Supplement',
        'description': '10 billion CFU probiotic blend. Supports digestive and immune health.',
        'manufacturer': 'GutHealth',
        'price': 18.99,
        'quantity_available': 65,
        'category': 'Digestive Health',
        'prescription_required': False
    }
]

# Clear existing data (optional - comment out if you want to keep existing data)
print("Clearing existing medicines...")
Medicine.objects.all().delete()

# Create medicines
print("\nCreating sample medicines...")
created_count = 0

for med_data in medicines_data:
    try:
        medicine = Medicine.objects.create(**med_data)
        created_count += 1
        print(f"✓ Created: {medicine.name}")
    except Exception as e:
        print(f"✗ Error creating {med_data['name']}: {str(e)}")

print(f"\n{'='*50}")
print(f"Successfully created {created_count} medicines!")
print(f"{'='*50}")

# Display summary
print("\nDatabase Summary:")
print(f"Total Medicines: {Medicine.objects.count()}")
print(f"Available Medicines: {Medicine.objects.filter(quantity_available__gt=0).count()}")
print(f"Prescription Required: {Medicine.objects.filter(prescription_required=True).count()}")

# Display categories
print("\nCategories:")
categories = Medicine.objects.values_list('category', flat=True).distinct()
for category in categories:
    count = Medicine.objects.filter(category=category).count()
    print(f"  - {category}: {count} items")

print("\n" + "="*50)
print("Sample data population complete!")
print("You can now start the server and browse the products.")
print("="*50)
