from django.shortcuts import render
from .models import Course , lesson


def index(request):

    courses = Course.objects.order_by("-id").first()
    return render(request, 'index.html', {"courses" : courses})

# Create your views here.


def detail(request):

    return render(request, 'detail.html')