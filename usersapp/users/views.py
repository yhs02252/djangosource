from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def users_login(request):
    return render(request, "users/login.html")
