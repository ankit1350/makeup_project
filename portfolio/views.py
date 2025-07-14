from django.shortcuts import render,HttpResponse
from datetime import datetime
from django.contrib import messages

from portfolio.models import Contact
def home(request):
    messages.info(request, "Welcome to our portfolio site!")
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')


def services(request):
    return render(request, 'portfolio/services.html')

def gallery(request):
    return render(request, 'portfolio/gallery.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request,"Thank you for contacting us! We will get back to you soon.")
    return render(request, "portfolio/contact.html")