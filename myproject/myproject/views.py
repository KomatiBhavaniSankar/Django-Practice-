from django.http import HttpResponse

def index(request):
    return HttpResponse('hello, this is the index view')

def about(request):
    return HttpResponse("this is the about")