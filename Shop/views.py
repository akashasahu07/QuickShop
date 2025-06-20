from django.shortcuts import render, redirect
from Shop.models import Product, CartItem
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/shop_page.html', {'products': products})

def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'Shop/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('shop:view_cart')

def remove_from_cart(request, product_id):
    cart_item = CartItem.objects.get(id=product_id, user=request.user)
    if cart_item.quantity == 1:
        cart_item.delete()
    else:
        cart_item.quantity -= 1
        cart_item.save()
    return redirect('shop:view_cart')

# Define a View function for the Registration Page
def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username already exists
        user = User.objects.filter(username=username)
        if user.exists():
            # Display an error message if the username is taken
            messages.error(request, 'Username already exists. Please choose a different one.')
            return redirect('/register/')
        
        # Create a new User object with the provided details
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )

        # Set the password for the new user
        user.set_password(password)
        user.save()

        # Display a success message and redirect to the login page
        messages.success(request, 'Registration successful! Please log in.')
        return redirect('/register/')
    
    # Render the registration page template
    return render(request, 'Shop/register.html', {'show_register': True})

# Define a View function for the Login Page
def login_page(request):
    # Check if the HTTP REQUEST method is POST
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the user does not exist
            messages.error(request, 'Invalid username.')
            return redirect('/login/')
        
        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)

        if user is None:
            # Display an error message if authentication fails
            messages.error(request, 'Invalid password.')
            return redirect('/login/')
        else:
            # Log in the user if authentication is successful
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('shop:product_list')
        
    # Render the login page template
    return render(request, 'Shop/login.html')
