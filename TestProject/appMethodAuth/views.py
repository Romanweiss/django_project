from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.contrib.auth.models import User


class AuthPage(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("urlAccountPage")
        return render(request, "appMethodAuth/auth.html")

    def post(self, request):
        username = request.POST["login"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("urlAccountPage")
            return HttpResponse("You are banned!!!")
        return HttpResponse("User is not available")


class AccountPage(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("urlAuthPage")
        return render(request, "appMethodAuth/account.html")


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("urlAuthPage")


class RegPage(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("urlAccountPage")
        return render(request, "appMethodAuth/reg.html")

    def post(self, request):
        username = request.POST["username"]
        user = User.objects.filter(username=username)
        if not user.exists():
            User.objects.create(
                username=username,
                last_name=request.POST['last_name'],
                first_name=request.POST['first_name'],
                password=make_password(request.POST['first_name']),
            )
            return redirect('urlAuthPage')
        return HttpResponse("You have to change nickname!")