"""SchoolInformationTransformSystem URL Configuration

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
from django.urls import path
from home.views import home
from anecdoteForum.views import anecdoteForum
from lostAndFound.views import lostAndFound
from driftBottle.views import driftBottle
from eventInformation.views import eventInformation
from loveWall.views import loveWall
from signIn.views import signIn


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'), 
    path('home/',home,name='home'), 
    path('home/<str:user>,<str:password>/',anecdoteForum,name='sign'),
    path('anecdoteForum/',anecdoteForum,name='anecdoteForum'),
    path('lostAndFound/',lostAndFound,name='lostAndFound'),
    path('driftBottle/',driftBottle,name='driftBottle'),
    path('eventInformation/',eventInformation,name='eventInformation'),
    path('loveWall/',loveWall,name='loveWall'),
    path('signIn',signIn,name='signIn'),
]
