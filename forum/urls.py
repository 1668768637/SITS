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
from django.urls import path
from .views import *


urlpatterns = [
    path('newPost',newPost,name='newPost'),
    path('delPost/<int:postId>',delPost,name='delPost'),
    path('commit',commit,name='commit'),
    path('delCommit/<int:id>',delCommit,name='delCommit'),
    path('likePost/<int:postId>',likePost,name="likePost"),
    path('<str:postType>',forum,name='forum'),
    path('findForumById/<int:postId>',findForumById,name='findForumById'),
    path('makeCollection/<int:postId>',makeCollection,name='makeCollection'),
    path('delCollection/<int:collectionId>',delCollection,name='delCollection'),
]
