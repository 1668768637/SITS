from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile,UserProfileManager
from django.http import JsonResponse
@csrf_exempt

# Create your views here.
def home(request):
    return render(request,'home.html',{'active_menu':'home'})



def log(request,logState):
    """
    :return:
    成功：重定向到首页
    失败:返回login页面,并提示错误
    """
    #if request.method == 'POST':
    sourceHtml = request.META['HTTP_REFERER']

    if logState == 'login':
        username = request.POST.get('user')
        password = request.POST.get('password')
        if username=='' or password=='':
            print("账号或密码为空")
            return JsonResponse({'error': '用户名或密码为空！',})
        else:
            print(username+"||"+password)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # 保存登录会话,将登陆的信息封装到request.user,包括session
                request.session['username']=user.get_username() 
                return JsonResponse({})
            else:
                return JsonResponse( {'error': '用户名或密码错误！',})
    else:
        if logState == 'logout':
            request.session['username'] = ""
            logout(request)
            return redirect(sourceHtml)


def signUp(request):
    username = request.POST.get('user')
    password = request.POST.get('password')
    user = UserProfile.objects.create_user(password=password,username=username)
    user.save()
    sourceHtml = request.META['HTTP_REFERER']
    return redirect(sourceHtml)

