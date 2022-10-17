from django.shortcuts import render
from .models import Posts

# Create your views here.


def home(request):
    return render(request, 'website/home.html', {
        "news": Posts.objects.all()
    })
