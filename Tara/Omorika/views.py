from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hi(request):
    #return HttpResponse('<h1>Home Page</h1>')
    return render(request, 'Omorika/index.html')
