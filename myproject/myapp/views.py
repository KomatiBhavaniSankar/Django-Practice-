from django.shortcuts import render
from django.http import HttpResponse

def mrectHome(request):
    return HttpResponse("this is myapp")