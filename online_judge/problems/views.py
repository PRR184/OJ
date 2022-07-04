from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Problem


# Create your views here.
def home(request):
    context = {
        'title': 'Problems',
        'problems':Problem.objects.all()
    }
    return render(request, 'problems/home.html',context)

@login_required
def details(request,problem_id):
    return render(request, 'problems/details.html',{"id":problem_id})

@login_required
def submissions(request):
    return render(request, 'problems/submissions.html')


