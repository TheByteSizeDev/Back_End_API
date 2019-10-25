"""dadmovesproject URL Configuration

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
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from dadmovesapi.models import Body_Region, Daddy_O, Difficulty_Type, Moves, Situation_Type
from dadmovesapi.views import register_user, login_user
from dadmovesapi.views import Body_Regions
from dadmovesapi.views import Daddy_Os
from dadmovesapi.views import Difficulty_Types
from dadmovesapi.views import Move
from dadmovesapi.views import Situation_Types

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'body_region', Body_Regions, 'body_region')
router.register(r'daddy_o', Daddy_Os, 'daddy_o')
router.register(r'difficulty_type', Difficulty_Types, 'difficulty_type')
router.register(r'moves', Move, 'moves')
router.register(r'situation_type', Situation_Types, 'situation_type')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^register$', register_user),
    url(r'^login$', login_user),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
