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


class ProfileRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    birthday = serializers.DateField()
    phone = serializers.IntegerField()
    password = serializers.CharField()
    password_confirm = serializers.CharField()

    def create(self, validated_data):
        if validated_data['password'] == validated_data['password_confirm']:
            user = Profile.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                birthday=validated_data['birthday'],
                phone=validated_data['phone'],
                password=validated_data['password']
            )
            return user
        else:
            return None
