from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
@csrf_exempt

# Create your views here.
# def home(request):
#     return render(request,'home.html',{'active_menu':'home'})

def home(request):
    return render(request, 'home.html')
    
    
def log(request,logState):
    """
    :return:
    成功：重定向到首页
    失败:返回login页面,并提示错误
    """
    #if request.method == 'POST':
    if logState == 'login':
        username = request.POST['username']
        password = request.POST['password']
        if(username=="" and password==""):
            print("kong")
            return render(request, 'home.html', {'error': '用户名户密码错误！',})
        print(username+"||"+password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)  # 保存登录会话,将登陆的信息封装到request.user,包括session
            request.session['username']=user.get_username()
            return redirect("/")
        else:
            return render(request, 'home.html', {'error': '用户名户密码错误！',})
    else:
        if logState == 'logout':
            request.session['username'] = ""
            my_logout(request)


def my_login(request):
    """
    :param request
    :return: 展示登录页面
    """
    return render(request, "login.html")


@login_required()
def   my_logout(request):
    """
    :param request
    :return: 退出并重定向到登录页面
    """
    logout(request)
    return redirect("/")


@login_required()
def index(request):
    """
    :param request
    :return: 用户首页
    """
    return render(request, "index.html")
