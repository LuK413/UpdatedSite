from django.shortcuts import render
from about.models import About


def home(request):
    about = About.objects.all()
    context = {
        "about": about
    }
    return render(request, "about.html", context)
