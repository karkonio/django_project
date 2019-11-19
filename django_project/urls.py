"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static


from . import views
from .api import api_urls, Login, CreateRegisterToken


urlpatterns = [
    path('api/register/', CreateRegisterToken.as_view()),
    path('api/auth/', Login.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(api_urls)),
    path('admin/', admin.site.urls),
    path('', views.home),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/<int:profile_id>/', views.profile),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
