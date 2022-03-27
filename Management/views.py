from .models import Contact as ContactModel
from django.shortcuts import redirect, render

def Home(request):
    return render(request, 'index-3.html')

def AboutUs(request):
    return render(request, 'about-us.html')

def Contact(request):
    if request.method == "POST":
        data = request.POST
        ContactModel.objects.create(name=data['name'], email=data['email'], subject = data['subject'], message = data['message'])
        return redirect('home')
    return render(request, "contact.html")