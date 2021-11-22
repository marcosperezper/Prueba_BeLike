from django.shortcuts import render
from .forms import RegistrationForm
from django.contrib.auth import login
from django.contrib.auth.models import User


# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request=request, template_name="home.html", context={'user': user})

    else:
        form = RegistrationForm()
        return render(request=request, template_name="register.html", context={"register_form": form})


def homepage(request):
    user = User.objects.all()
    return render(request=request, template_name="home.html", context={'user': user})
