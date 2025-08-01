from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect  # ✅ you missed importing redirect

def contact(request):
    return HttpResponse("this is myapp")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  # ✅ make sure 'contact' is a valid URL name
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})  # ✅ Always returns HttpResponse
