from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.utils.http import is_safe_url

# Create your views here.
from .forms import SignUpForm
from .models import SignUp

User = get_user_model()
def registeration(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        primary_email  = form.cleaned_data.get("primary_email")
        password  = form.cleaned_data.get("password")
        new_user  = User.objects.create_user( primary_email, password)

    return render(request, "registration/register.html", context)
