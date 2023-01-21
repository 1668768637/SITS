from django.shortcuts import render,redirect
from home.models import UserProfile,UserProfileManager

# Create your views here.

def anecdoteForum(request):
    return render(request,'anecdoteForum.html',{'active_menu':'anecdoteForum'})

def lostAndFound(request):
    return render(request,'lostAndFound.html',{'active_menu':'lostAndFound'})

def driftBottle(request):
    return render(request,'driftBottle.html',{'active_menu':'driftBottle'})

def eventInformation(request):
    return render(request,'eventInformation.html',{'active_menu':'eventInformation'})
    
def loveWall(request):
    return render(request,'loveWall.html',{'active_menu':'loveWall'})