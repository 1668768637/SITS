from django.shortcuts import render

# Create your views here.
def loveWall(request):
    return render(request,'loveWall.html',{'active_menu':'loveWall'})