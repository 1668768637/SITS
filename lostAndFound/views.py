from django.shortcuts import render

# Create your views here.
def lostAndFound(request):
    return render(request,'lostAndFound.html',{'active_menu':'lostAndFound'})