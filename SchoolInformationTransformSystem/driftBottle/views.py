from django.shortcuts import render

# Create your views here.
def driftBottle(request):
    return render(request,'driftBottle.html',{'active_menu':'driftBottle'})