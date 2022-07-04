from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

from .models import Problem


# Create your views here.
def home(request):
    context = {
        'title': 'Problems',
        'problems':Problem.objects.all()
    }
    return render(request, 'problems/home.html',context)

def details(request,problem_id):
    return render(request, 'problems/details.html',{"id":problem_id})

def submissions(request):
    return render(request, 'problems/submissions.html')


