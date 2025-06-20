from django.shortcuts import render



def home(request):
    return render(request, 'templates/portfolio/home.html"')

def about(request):
    print("✅ This is the about view")  # Debug print
    return render(request, 'portfolio/about.html')


def services(request):
    return render(request, 'portfolio/services.html')

def gallery(request):
    return render(request, 'portfolio/gallery.html')

def contact(request):
    return render(request, 'portfolio/contact.html')
