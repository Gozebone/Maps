from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, "home.html")

def signup_view(request, *args, **kwargs):
    return render(request, "signup.html")
