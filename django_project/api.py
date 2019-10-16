from rest_framework.viewsets import ModelViewSet
from rest_framework import routers, permissions

from .models import Post, Profile
from .serializers import PostSerializer, ProfileSerializer


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class ProfileViewSet(ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    permission_classes = (permissions.IsAuthenticated,)


router = routers.SimpleRouter()
router.register(r'posts', PostViewSet)
router.register(r'profiles', ProfileViewSet)
api_urls = router.urls
