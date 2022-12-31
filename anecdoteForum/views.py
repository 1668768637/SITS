from django.shortcuts import render

# Create your views here.
def anecdoteForum(request):
    return render(request,'anecdoteForum.html',{'active_menu':'anecdoteForum'})