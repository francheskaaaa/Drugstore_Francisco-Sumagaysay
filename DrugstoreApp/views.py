from django.shortcuts import render


def login_view(request):
    if request.method == "POST":
        # Add authentication logic here
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Example logic (use Django's authentication system for production):
        if username == "admin" and password == "password":
            return render(request, 'success.html')  # Or redirect to another page
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

def home_view(request):

    return render(request, 'home.html')

def inventory_view(request):

    return render(request, 'inventory.html')

def product_view(request):

    return render(request, 'product.html')

def customer_view(request):

    return render(request, 'customer.html')

def sales_view(request):

    return render(request, 'sales.html')

def supplier_view(request):

    return render(request, 'supplier.html')

def user_view(request):

    return render(request, 'user.html')

def report_view(request):

    return render(request, 'report.html')

def auditlog_view(request):

    return render(request, 'auditLog.html')

def create_view(request):

    return render(request, 'create.html')