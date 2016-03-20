# -​*- coding: utf-8 -*​-
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, "index.html")

def signin(request):
    return render(request, "signin.html")

def about(request):
    return render(request, "about.html")

def signup(request):
    error = None
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        # Sign up user

        # Password match
        if password != password2:
            error = "비밀번호가 일치하지 않습니다."

        # Username exist
        users = User.objects.filter(username=username)
        if len(users) > 0:
            error = "이 아이디로 가입 된 유저가 있습니다."

        # Email exist
        users = User.objects.filter(email=email)
        if len(users) > 0:
            error = "이 이메일로 가입 된 유저가 있습니다."

        if error is None:
            # Sign up user
            user = User.objects.create_user(username, email, password)
            user.save()
            return redirect('user')
    return render(request, "signup.html", { "error": error })

def order(request):
    return render(request, "order.html")

def user(request):
    return render(request, "user.html")
