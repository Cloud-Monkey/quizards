from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView


from . forms import UserRegistrationForm, UserLoginForm


# Create your views here.
class QuizPage(TemplateView):
    """
    Displays quiz page
    """
    template_name = 'quiz.html'


class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = 'base.html'


class UserRegistrationView(CreateView):
    """
    Displays user registration page and handles user registration
    """
    form_class = UserRegistrationForm
    template_name = "accounts/registration/registration-user.html"
    success_url = reverse_lazy('user_registration_success')
    

class UserSuccessView(TemplateView):
    """
    Displays user registration success page
    """
    template_name = "accounts/registration/registration-success.html"

class UserLoginView(LoginView):
    """
    Displays login page
    """
    form_class = UserLoginForm
    template_name = 'accounts/login-user.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return self.success_url

# logout
class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')