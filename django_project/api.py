from django.db import IntegrityError

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import routers, status

from .models import Post, Profile, Follower
from .serializers import \
    ProfileSerializer, ProfileDetailSerializer, PostDetailSerializer,\
    FollowerCreateSerializer


class Login(ObtainAuthToken):

    def post(self, request):
        serializer = super().serializer_class(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.id
        })


class MultiSerializerViewSetMixin(object):
    def get_serializer_class(self):  # pragma: no cover
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super(MultiSerializerViewSetMixin, self).get_serializer_class()  # noqa


class PostViewSet(ModelViewSet):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    read_only = True


class ProfileViewSet(MultiSerializerViewSetMixin, ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    serializer_action_classes = {
        'list': ProfileSerializer,
        'retrieve': ProfileDetailSerializer
    }


class FollowView(ModelViewSet):
    queryset = Follower.objects.all()
    serializer_class = FollowerCreateSerializer

    def create(self, request):
        data = request.data

        current_user_id = data.get('current_user_id')
        profile_id = data.get('profile_id')
        try:
            follower = Profile.objects.get(id=current_user_id)
            following = Profile.objects.get(id=profile_id)

            if follower != following:
                # if all is OK --> follow object create
                try:
                    Follower.objects.create(follower=follower,
                                            following=following)
                    return Response(status=status.HTTP_201_CREATED,
                                    data='follow')

                # if already exists --> follow object delete
                except IntegrityError:  # pragma: no cover
                    Follower.objects.get(follower=follower,
                                         following=following).delete()  # noqa
                    return Response(
                        status=status.HTTP_201_CREATED,
                        data='unfollow'
                    )
            else:  # pragma: no cover
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data='can`t follow yourself'
                )

        except IndexError:  # pragma: no cover
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data='profile does not exist'
            )


router = routers.SimpleRouter()
router.register('posts', PostViewSet)
router.register('profiles', ProfileViewSet)
router.register('follow', FollowView)
api_urls = router.urls
