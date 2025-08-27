from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

def index(request):
    return render(request, "components/index.html")

def navigation(request):
    return render(request, "layouts/navigation.html")

def user_login(request):
    if request.method == "post":
        username = request.post.get("username")
        password = request.post.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("Home")
        else:
            return render(request, "login.html", {"error_message": "Invalid username or password."})

# Create your views here.
