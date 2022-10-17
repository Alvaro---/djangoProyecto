from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# from posts.models import Posts

# Create your views here.


def wellcome(request):
    return render(request, 'website/wellcome.html', {
        "info": "Este curso es malo",
        "suma": 5+2
    })


def date(request):
    return HttpResponse('la hora sel server es: '+str(datetime.now()))


def not_found(request, exception):
    return render(request, 'website/404.html', status=404)


def home(request):
    return render(request, 'website/home.html', {
        "countNews": Posts.objects.count(),
        "news": Posts.objects.all()
    })


def jobs(request):
    return render(request, "website/jobs.html", {
        "jobs": "Pagina proyecto",
        # "allJobs": Posts.objects.all()
    })
