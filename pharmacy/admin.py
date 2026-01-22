from django.contrib import admin
from .models import Medicine, Cart, Order, OrderItem

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ['name', 'manufacturer', 'price', 'quantity_available', 
                    'quantity_sold', 'is_available', 'category', 'created_at']
    list_filter = ['prescription_required', 'category', 'created_at']
    search_fields = ['name', 'manufacturer', 'description']
    readonly_fields = ['quantity_sold', 'created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'manufacturer', 'category')
        }),
        ('Pricing and Stock', {
            'fields': ('price', 'quantity_available', 'quantity_sold')
        }),
        ('Additional Info', {
            'fields': ('image', 'prescription_required', 'created_at', 'updated_at')
        }),
    )


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'medicine', 'quantity', 'subtotal', 'added_at']
    list_filter = ['added_at']
    search_fields = ['user__username', 'medicine__name']
    readonly_fields = ['added_at']


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['medicine', 'quantity', 'price', 'subtotal']
    can_delete = False


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'user', 'total_amount', 'status', 
                    'created_at', 'confirmed_at']
    list_filter = ['status', 'created_at']
    search_fields = ['order_number', 'user__username']
    readonly_fields = ['order_number', 'created_at', 'updated_at', 'confirmed_at']
    inlines = [OrderItemInline]
    
    fieldsets = (
        ('Order Information', {
            'fields': ('order_number', 'user', 'status', 'total_amount')
        }),
        ('Shipping Details', {
            'fields': ('shipping_address', 'contact_number')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'confirmed_at')
        }),
    )
    
    def save_model(self, request, obj, form, change):
        if change and 'status' in form.changed_data and obj.status == 'confirmed':
            obj.confirm_order()
        else:
            super().save_model(request, obj, form, change)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'medicine', 'quantity', 'price', 'subtotal']
    list_filter = ['order__created_at']
    search_fields = ['order__order_number', 'medicine__name']
