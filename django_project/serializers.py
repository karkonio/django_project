from rest_framework import serializers

from .models import Post, Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id', 'username', 'birthday', 'first_name', 'last_name', 'age',
            'zodiac', 'phone', 'website', 'city', 'posts'
        ]


class PostSerializer(serializers.ModelSerializer):
    profile = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    created = serializers.DateTimeField(format="%d %B, %Y  %H:%M")

    class Meta:
        model = Post
        fields = ['id', 'image', 'description', 'profile', 'created']


class ProfileDetailSerializer(ProfileSerializer):
    posts = PostSerializer(many=True)
