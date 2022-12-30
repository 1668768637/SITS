from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def signIn(request):
    print(request.POST.get('user') + request.POST.get('password'))
    return HttpResponse('OK')