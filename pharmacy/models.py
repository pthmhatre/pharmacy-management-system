from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.utils import timezone

class Medicine(models.Model):
    """Model to store medicine inventory"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    manufacturer = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    quantity_available = models.IntegerField(validators=[MinValueValidator(0)])
    quantity_sold = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to='medicines/', blank=True, null=True)
    prescription_required = models.BooleanField(default=False)
    category = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Medicines'
    
    def __str__(self):
        return self.name
    
    @property
    def is_available(self):
        """Check if medicine is in stock"""
        return self.quantity_available > 0
    
    @property
    def total_quantity(self):
        """Total quantity including sold items"""
        return self.quantity_available + self.quantity_sold
    
    def reduce_stock(self, quantity):
        """Reduce stock after sale"""
        if self.quantity_available >= quantity:
            self.quantity_available -= quantity
            self.quantity_sold += quantity
            self.save()
            return True
        return False


class Cart(models.Model):
    """Model to store user cart items"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1)], default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'medicine')
        ordering = ['-added_at']
    
    def __str__(self):
        return f"{self.user.username}'s cart - {self.medicine.name}"
    
    @property
    def subtotal(self):
        """Calculate subtotal for this cart item"""
        return self.quantity * self.medicine.price
    
    def is_quantity_available(self):
        """Check if requested quantity is available in stock"""
        return self.medicine.quantity_available >= self.quantity


class Order(models.Model):
    """Model to store completed orders"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    order_number = models.CharField(max_length=100, unique=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    shipping_address = models.TextField()
    contact_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    confirmed_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Order {self.order_number} - {self.user.username}"
    
    def confirm_order(self):
        """Confirm the order"""
        self.status = 'confirmed'
        self.confirmed_at = timezone.now()
        self.save()


class OrderItem(models.Model):
    """Model to store individual items in an order"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return f"{self.medicine.name} x {self.quantity}"
    
    @property
    def subtotal(self):
        """Calculate subtotal for this order item"""
        return self.quantity * self.price
