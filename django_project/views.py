from django.shortcuts import render


from .models import Image, Profile


def home(request):
    images = Image.objects.all()
    return render(request, 'home.html', context={
        'images': images
    })


def profile(request):
    profiles = Profile.objects.all()
    return render(request, 'profile.html', context={
        'users': profiles
    })
