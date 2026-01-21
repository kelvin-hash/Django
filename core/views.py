from django.shortcuts import render, redirect
from .models import Job, Freelancer
from .forms import JobForm, FreelancerForm
from django.http import HttpResponse
from .serializer import JobSerializer, FreelancerSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = JobForm()

    return render(request, 'core/job_form.html', {'form': form})


def create_freelancer(request):
    if request.method == 'POST':
        form = FreelancerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_freelancer')
    else:
        form = FreelancerForm()

    return render(request, 'core/create_freelancer.html', {'form': form})


def freelancer_list(request):
    freelancers = Freelancer.objects.all()
    return render(request, 'core/freelancer_list.html', {'freelancers': freelancers})


def home(request):
    freelancers = Freelancer.objects.all()
    jobs = Job.objects.all()
    return render(request, 'core/home.html', {
        'freelancers': freelancers,
        'jobs': jobs
    })

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'core/job_list.html', {'jobs': jobs})

def hello_world(request):
    return HttpResponse("Hello, World!")

@api_view(['GET'])
def job_list_api(request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)
