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
from django.urls.conf import include

from home.views import *
from user.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'), 
    path('home',home,name='home'), 
    path('forum/',include('forum.urls')),
    path('log/<str:logState>/',log,name='log'),
    path('signUp',signUp,name='signUp'),
    path('forgetPassword/<str:username>',forgetPassword,name='forgetPassword'),
    path('userInfo/<str:username>',userInfo,name='userInfo'),
    path('modifyInfo',modifyInfo,name='modifyInfo'),
    path('delUser',delUser,name='delUser'),
    path('readMessage/<int:msgId>',readMessage,name='readMessage'),
    path('search',search,name="search")
]

#加入media文件夹支持
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
