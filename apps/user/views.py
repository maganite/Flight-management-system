from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import authenticate, login

from .models import User
from .forms import SignUpForm, LoginForm


class IsUserAuthenticatedMixin:
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("dashboard:index")
        form = self.form_class()
        return render(request, self.template_name, {"form": form})


class UserLoginView(IsUserAuthenticatedMixin, View):
    form_class = LoginForm
    template_name = "accounts/auth-signin.html"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            status = User.objects.filter(email=email)
            if user is not None:
                login(request, user)
                return redirect("dashboard:index")
            elif status.values() and not status.values()[0]["is_active"]:
                form.add_error(None, "Your account is not been verified")
            else:
                form.add_error(None, "Invalid login credentials")
        return render(request, self.template_name, {"form": form})


class UserRegisterView(CreateView):
    template_name = "accounts/auth-signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("dashboard:index")

    
class UserLogoutView(LogoutView):
    next_page = "user:login"
