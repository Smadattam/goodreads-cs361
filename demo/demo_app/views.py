from pyexpat.errors import messages
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Book, Review, User

# Create your views here.
def home(request):
    return render(request, "home.html")

def books(request):
    book_list = Book.objects.all()
    return render(request, "books/book_list.html", {"book_list": book_list})

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.success(request, "Invalid credentials, please try again.")
            return render(request, "authenticate/login.html", {"error": "Invalid credentials"})
    return render(request, "authenticate/login.html", {})