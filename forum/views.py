from django.shortcuts import render

# Create your views here.
def forum(request,postType):
    return render(request,'test.html')