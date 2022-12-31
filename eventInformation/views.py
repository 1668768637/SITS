from django.shortcuts import render

# Create your views here.
def eventInformation(request):
    return render(request,'eventInformation.html',{'active_menu':'eventInformation'})