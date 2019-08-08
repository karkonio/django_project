from django.shortcuts import render


from .models import Image, Profile


def home(request):
    images = Image.objects.all()
    return render(request, 'home.html', context={
        'images': images
    })


def profile(request, user_id):
    profile = Profile.objects.get(user_id=user_id)
    tags = profile.tags.split(',')
    return render(request, 'profile.html', context={
        'users': profile,
        'tags': tags
    })
