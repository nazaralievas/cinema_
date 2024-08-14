from django.shortcuts import render

def homepage(request):
    return render(request, 'core/homepage.html')

def rules(request):
    return render(request, 'core/rules.html')