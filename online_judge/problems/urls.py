from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "problems-home"),
    path('<int:problem_id>/details/', views.details, name = "problems-details"),
    path('submissions/', views.submissions, name = "problems-submissions"),
]