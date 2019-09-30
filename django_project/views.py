from django.shortcuts import render

from .models import Profile, Post


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', context={
        'posts': posts
    })


def profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    following = profile.following.all().count()
    followers = profile.followers.all().count()
    return render(request, 'profile.html', context={
        'profile': profile,
        'following': following,
        'followers': followers
    })
