from rest_framework.viewsets import ModelViewSet
from rest_framework import routers

from .models import Post
from .serializers import PostSerializer


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


router = routers.SimpleRouter()
router.register(r'posts', PostViewSet)
api_urls = router.urls