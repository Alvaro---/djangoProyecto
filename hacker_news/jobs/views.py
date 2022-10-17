from django.shortcuts import render
from .models import Jobs

# Create your views here.


def jobs(request):
    return render(request, 'website/jobs.html', {
        "allJobs": Jobs.objects.all()
    })
