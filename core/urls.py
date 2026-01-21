from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/create/', views.create_job, name='create_job'),
    path('freelancers/create/', views.create_freelancer, name='create_freelancer'),
    path('freelancers/', views.freelancer_list, name='freelancer_list'),
    path('hello/', views.hello_world, name='hello_world'),
    path('api/jobs/', views.job_list_api, name='job_list_api'),
]
