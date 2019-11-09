from rest_framework import serializers

from .models import Post, Profile


class ProfileSerializer(serializers.ModelSerializer):
    following_count = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            'id', 'username', 'birthday', 'first_name', 'last_name', 'age',
            'zodiac', 'phone', 'website', 'city', 'posts', 'avatar',
            'following_count', 'followers_count', 'direction'
        ]

    def get_following_count(self, obj):
        return obj.following.count()  # pragma: no cover

    def get_followers_count(self, obj):
        return obj.followers.count()  # pragma: no cover


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


class ProfileForPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'username']


class PostDetailSerializer(PostSerializer):
    profile = ProfileForPostSerializer()
