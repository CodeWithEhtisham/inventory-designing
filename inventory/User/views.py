from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
# Create your views here.
def defLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            messages.error(request,"Invalid User")
            return render(request, 'login.html')
    return render(request, 'login.html')