from django.shortcuts import render
from .models import Job

def index(request):
    jobs = Job.objects
    return render(request, 'jobs/index.html', {'jobs': jobs})