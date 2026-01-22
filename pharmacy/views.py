from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Sum
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import uuid
from .models import Medicine, Cart, Order, OrderItem
from .forms import UserRegisterForm, UserLoginForm, OrderCheckoutForm, SearchForm

def home(request):
    """Home page view with featured medicines"""
    medicines = Medicine.objects.filter(quantity_available__gt=0)[:8]
    search_form = SearchForm()
    
    context = {
        'medicines': medicines,
        'search_form': search_form,
    }
    return render(request, 'home.html', context)


def about(request):
    """About page view"""
    return render(request, 'about.html')


def contact(request):
    """Contact page view"""
    if request.method == 'POST':
        messages.success(request, 'Thank you for your message! We will get back to you soon.')
        return redirect('contact')
    return render(request, 'contact.html')


def register_view(request):
    """User registration view"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    
    return render(request, 'register.html', {'form': form})


def login_view(request):
    """User login view"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                next_url = request.GET.get('next', 'home')
                return redirect(next_url)
    else:
        form = UserLoginForm()
    
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    """User logout view"""
    if request.user.is_authenticated:
        username = request.user.username
        logout(request)
        messages.info(request, f'Goodbye, {username}! You have been logged out.')
    return render(request, 'logout.html')


def products_view(request):
    """Products listing page with search and filtering"""
    search_query = request.GET.get('search', '')
    category = request.GET.get('category', '')
    
    medicines = Medicine.objects.all()
    
    if search_query:
        medicines = medicines.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(manufacturer__icontains=search_query) |
            Q(category__icontains=search_query)
        )
    
    if category:
        medicines = medicines.filter(category__icontains=category)
    
    # Get all unique categories
    categories = Medicine.objects.values_list('category', flat=True).distinct()
    
    context = {
        'medicines': medicines,
        'search_query': search_query,
        'categories': categories,
        'selected_category': category,
        'search_form': SearchForm(initial={'query': search_query}),
    }
    return render(request, 'products.html', context)


def search_medicines(request):
    """Search medicines - AJAX endpoint"""
    query = request.GET.get('query', '')
    
    if query:
        medicines = Medicine.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(manufacturer__icontains=query)
        )[:10]
        
        results = []
        for medicine in medicines:
            results.append({
                'id': medicine.id,
                'name': medicine.name,
                'price': str(medicine.price),
                'available': medicine.is_available,
                'quantity': medicine.quantity_available,
            })
        
        return JsonResponse({'results': results})
    
    return JsonResponse({'results': []})


@login_required
def add_to_cart(request, medicine_id):
    """Add medicine to cart"""
    medicine = get_object_or_404(Medicine, id=medicine_id)
    
    if not medicine.is_available:
        messages.error(request, f'{medicine.name} is currently out of stock.')
        return redirect(request.META.get('HTTP_REFERER', 'home'))
    
    quantity = int(request.POST.get('quantity', 1))
    
    if quantity > medicine.quantity_available:
        messages.error(request, f'Only {medicine.quantity_available} units of {medicine.name} are available.')
        return redirect(request.META.get('HTTP_REFERER', 'home'))
    
    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        medicine=medicine,
        defaults={'quantity': quantity}
    )
    
    if not created:
        new_quantity = cart_item.quantity + quantity
        if new_quantity > medicine.quantity_available:
            messages.error(request, f'Cannot add more. Only {medicine.quantity_available} units available.')
            return redirect(request.META.get('HTTP_REFERER', 'home'))
        cart_item.quantity = new_quantity
        cart_item.save()
        messages.success(request, f'Updated {medicine.name} quantity in cart.')
    else:
        messages.success(request, f'{medicine.name} added to cart!')
    
    return redirect(request.META.get('HTTP_REFERER', 'home'))


@login_required
def cart_view(request):
    """Shopping cart view"""
    cart_items = Cart.objects.filter(user=request.user)
    
    total = sum(item.subtotal for item in cart_items)
    
    # Check for unavailable items
    unavailable_items = [item for item in cart_items if not item.is_quantity_available()]
    if unavailable_items:
        for item in unavailable_items:
            messages.warning(request, f'{item.medicine.name} - Requested quantity not available.')
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'unavailable_items': unavailable_items,
    }
    return render(request, 'cart.html', context)


@login_required
@require_POST
def update_cart(request, cart_id):
    """Update cart item quantity"""
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    quantity = int(request.POST.get('quantity', 1))
    
    if quantity <= 0:
        cart_item.delete()
        messages.info(request, 'Item removed from cart.')
    elif quantity > cart_item.medicine.quantity_available:
        messages.error(request, f'Only {cart_item.medicine.quantity_available} units available.')
    else:
        cart_item.quantity = quantity
        cart_item.save()
        messages.success(request, 'Cart updated.')
    
    return redirect('cart')


@login_required
@require_POST
def remove_from_cart(request, cart_id):
    """Remove item from cart"""
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    medicine_name = cart_item.medicine.name
    cart_item.delete()
    messages.info(request, f'{medicine_name} removed from cart.')
    return redirect('cart')


@login_required
def checkout(request):
    """Checkout and create order"""
    cart_items = Cart.objects.filter(user=request.user)
    
    if not cart_items:
        messages.error(request, 'Your cart is empty.')
        return redirect('cart')
    
    # Check stock availability
    for item in cart_items:
        if not item.is_quantity_available():
            messages.error(request, f'{item.medicine.name} - Insufficient stock.')
            return redirect('cart')
    
    if request.method == 'POST':
        form = OrderCheckoutForm(request.POST)
        if form.is_valid():
            # Calculate total
            total = sum(item.subtotal for item in cart_items)
            
            # Create order
            order = Order.objects.create(
                user=request.user,
                order_number=f'ORD-{uuid.uuid4().hex[:8].upper()}',
                total_amount=total,
                shipping_address=form.cleaned_data['shipping_address'],
                contact_number=form.cleaned_data['contact_number'],
                status='pending'
            )
            
            # Create order items and update stock
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    medicine=item.medicine,
                    quantity=item.quantity,
                    price=item.medicine.price
                )
                # Reduce stock
                item.medicine.reduce_stock(item.quantity)
            
            # Clear cart
            cart_items.delete()
            
            messages.success(request, f'Order {order.order_number} placed successfully! Awaiting confirmation.')
            return redirect('order_detail', order_id=order.id)
    else:
        form = OrderCheckoutForm()
    
    total = sum(item.subtotal for item in cart_items)
    
    context = {
        'form': form,
        'cart_items': cart_items,
        'total': total,
    }
    return render(request, 'checkout.html', context)


@login_required
def order_detail(request, order_id):
    """Order detail view"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    context = {
        'order': order,
    }
    return render(request, 'order_detail.html', context)


@login_required
@require_POST
def confirm_order(request, order_id):
    """Confirm order"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    if order.status == 'pending':
        order.confirm_order()
        messages.success(request, f'Order {order.order_number} confirmed!')
    else:
        messages.info(request, 'Order already confirmed.')
    
    return redirect('order_detail', order_id=order.id)


@login_required
def my_orders(request):
    """View user's orders"""
    orders = Order.objects.filter(user=request.user)
    
    context = {
        'orders': orders,
    }
    return render(request, 'my_orders.html', context)
