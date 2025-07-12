# views.py
from django.shortcuts import render, redirect
import qrcode
import io
import base64
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Registration failed. Please correct the errors.')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Your password must be at least 8 characters long, contain at least one number')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')

# Main QR code generator view - protected
@login_required(login_url='login')
def index(request):
    qr_image_base64 = None
    data = ''
    message = ''
    if request.method == 'POST':
        data = request.POST.get('data', '')
        if data:
            # Generate QR code
            qr = qrcode.QRCode(
                version=1,
                box_size=10,
                border=4
            )
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill_color='black', back_color='white')

            # Save image to BytesIO
            buffer = io.BytesIO()
            img.save(buffer, format='PNG')
            image_png = buffer.getvalue()
            buffer.close()

            # Encode image to base64
            qr_image_base64 = base64.b64encode(image_png).decode('utf-8')
        else:
            message = 'Please enter some data or URL.'
    return render(request, 'index.html', {
        'qr_image': qr_image_base64,
        'data': data,
        'message': message
    })