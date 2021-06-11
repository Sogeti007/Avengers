from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        'title': 'This'
    }
    return render(request, 'main/main.html', context)
