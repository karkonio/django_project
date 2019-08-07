from django.shortcuts import render


from .models import Image


def home(request):
    images = Image.objects.all()
    return render(request, 'home.html', context={
        'images': images
    })


def profile(request):
    return render(request, 'profile.html')
