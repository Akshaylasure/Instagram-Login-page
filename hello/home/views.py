from django.shortcuts import render
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        #desc = request.POST.get('desc')
    

        index = Contact(name=name, email=email)#desc=desc)
        index.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'index.html')
    

