from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import routers, status

from django_project.email import send_email
from .models import Post, Profile
from .serializers import \
    ProfileSerializer, ProfileDetailSerializer, PostDetailSerializer,\
    ProfileRegistrationSerializer


class CreateRegisterToken(APIView):

    def post(self, request):
        profile = ProfileRegistrationSerializer().create(validated_data=request.data)  # noqa
        if profile is not None:
            profile.save()
            activation_token = PasswordResetTokenGenerator().make_token(profile)  # noqa
            send_email(profile, activation_token)
            return Response(status=status.HTTP_201_CREATED)
        else:  # pragma: no cover
            return Response({
                'Passwords do not match or this data already exists.'
            }, status=status.HTTP_400_BAD_REQUEST)


class AccountActivation(APIView):

    def get(self, request, token, username):  # pragma: no cover
        try:
            profile = Profile.objects.get(username=username)
            # returns True or False
            if PasswordResetTokenGenerator().check_token(profile, token):
                profile.set_password(profile.password)
                profile.save()
            return Response("Account successfully activated", status=status.HTTP_201_CREATED)  # noqa
        except Profile.DoesNotExist:
            return Response("Bad credentials", status=status.HTTP_400_BAD_REQUEST)  # noqa


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
    parser_classes = [MultiPartParser]

    def create(self, request):  # pragma: no cover
        try:
            description = request.data.get('description')
            profile_id = request.data.get('current_user_id')
            profile = Profile.objects.get(id=profile_id)

            if request.data.get('file') is not None:
                post_image = self.request.data.get('file')
            else:
                return Response("Image not uploaded", status=status.HTTP_400_BAD_REQUEST)  # noqa

            Post.objects.create(
                profile=profile,
                image=post_image,
                description=description
            )
            return Response('Post successfully created', status=status.HTTP_201_CREATED)  # noqa
        except Profile.DoesNotExist:
            return Response("User undefined", status=status.HTTP_400_BAD_REQUEST)  # noqa


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
