from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def signin(request):
    return render(request, "signin.html")

def about(request):
    return render(request, "about.html")

def signup(request):
    return render(request, "signup.html")

def order(request):
    return render(request, "order.html")

def user(request):
    return render(request, "user.html")
