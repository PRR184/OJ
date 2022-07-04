from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

problems = [
    {
        'id':1,
        'title':'Two Sum',
        'difficulty':'Easy'
    },
    {
        'id':2,
        'title':'Three Sum',
        'difficulty':'Medium'
    }
]

# Create your views here.
def home(request):
    context = {
        'title': 'Problems',
        'problems':problems
    }
    return render(request, 'problems/home.html',context)

def details(request,question_id):
    return render(request, 'problems/details.html')

def submissions(request):
    return HttpResponse(f'Submissions Page')

