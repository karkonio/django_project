from django.shortcuts import render


from .models import Post, Profile


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', context={
        'posts': posts
    })


def profile(request, user_id):
    profile = Profile.objects.get(user_id=user_id)
    age = profile.age()
    zodiac = profile.zodiac()
    return render(request, 'profile.html', context={
        'user': profile,
        'age': age,
        'zodiac': zodiac
    })
