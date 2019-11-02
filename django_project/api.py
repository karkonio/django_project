from rest_framework.viewsets import ModelViewSet
from rest_framework import routers

from .models import Post, Profile
from .serializers import \
    PostSerializer, ProfileSerializer, ProfileDetailSerializer


class MultiSerializerViewSetMixin(object):
    def get_serializer_class(self):  # pragma: no cover
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super(MultiSerializerViewSetMixin, self).get_serializer_class()  # noqa


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    read_only = True


class ProfileViewSet(MultiSerializerViewSetMixin, ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    serializer_action_classes = {
        'list': ProfileSerializer,
        'retrieve': ProfileDetailSerializer,
    }
    read_only = True


router = routers.SimpleRouter()
router.register('posts', PostViewSet)
router.register('profiles', ProfileViewSet)
api_urls = router.urls
