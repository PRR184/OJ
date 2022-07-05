from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages

from .models import Problem, Submission

import os,filecmp, subprocess

BASE_DIR = settings.BASE_DIR

# Create your views here.
def home(request):
    context = {
        'title': 'Problems',
        'problems':Problem.objects.all()
    }
    return render(request, 'problems/home.html',context)

@login_required
def details(request,problem_id):
    problem = get_object_or_404(Problem,pk=problem_id)
    if request.method == 'POST':
        file = request.FILES['solution']
        code = ""
        with open('./solution.cpp','wb+') as f:
            for chunk in file.chunks():
                f.write(chunk)
                code += chunk.decode('utf-8')
        # Compile the Code
        compiled = subprocess.run('g++ ./solution.cpp', shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if compiled.returncode != 0:
            messages.warning(request, f'{compiled.stderr}')
            submission = Submission(user=request.user,problem=problem,verdict = "Compilation Error",submitted_code=code)    
            submission.save()  
            return render(request, 'problems/details.html',{'problem':problem})
        

        inputfile = os.path.join(os.getcwd(),'testcases','input',f'{problem_id}')

        for filename in os.listdir(inputfile):
            input_file = f".\\testcases\\input\\{problem_id}\\{filename}"
            actual_output = f".\\testcases\\output\\{problem_id}\\{filename}"

            os.system(f'a.exe < {input_file} > out.txt')              
            if(filecmp.cmp('out.txt',actual_output, shallow=False) == False):
                testcaseNumber = filename.split('.')[0]
                messages.warning(request, f'Your code gave Wrong Answer on TestCase {testcaseNumber}!')
                submission = Submission(user=request.user,problem=problem,verdict = f"Wrong Answer on TestCase {testcaseNumber}",submitted_code=code)    
                submission.save()       
                return render(request, 'problems/details.html',{'problem':problem})

        submission = Submission(user=request.user,problem=problem,verdict = "Accepted",submitted_code=code)    
        submission.save()                          
        messages.success(request, 'Your code got Accepted!')
        return render(request, 'problems/details.html',{'problem':problem})
    return render(request, 'problems/details.html',{'problem':problem})

@login_required
def submissions(request):
    submissions = Submission.objects.all()
    return render(request, 'problems/submissions.html',{'submissions': submissions})


