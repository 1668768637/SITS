from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout,password_validation
from django.core.exceptions import ValidationError
from .models import UserProfile
from forum.models import Post
from django.http import JsonResponse
@csrf_exempt

# Create your views here.
def home(request):
    postList = Post.objects.all().order_by("-likesNum")
    return render(request,'home.html',{'active_menu':'home','postList':postList})



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
            return JsonResponse({'logError': '用户名或密码为空！',})
        else:
            print(username+"||"+password)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # 保存登录会话,将登陆的信息封装到request.user,包括session
                request.session['nickName']=user.get_nickName()
                request.session['userError']=""
                return JsonResponse({})
            else:
                return JsonResponse( {'logError': '用户名或密码错误！',})
    else:
        if logState == 'logout':
            request.session['nickName'] = ""
            logout(request)
            return redirect(sourceHtml)


def signUp(request):
    username = request.POST.get('user')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    errors = []

    if username == '':
        errors.append("用户名不能为空")
    else:
        if len(username) < 6:
            errors.append("用户名太短")
        if UserProfile.objects.filter(username=username).exists():
            errors.append("用户名不唯一")

    if password1 == '':
        errors.append("密码不能为空")
    else:
        if password1 != password2:
            errors.append("两个密码不相等")
        else:
            if len(password1) < 8:
                errors.append("密码少于八个字符")
            try:
                password_validation.validate_password(password=password1,password_validators=password_validation.get_password_validators([
                    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
                    ]))
            except ValidationError :
                errors.append("密码不能是纯数字")
            try:
                password_validation.validate_password(password=password1,password_validators=password_validation.get_password_validators([
                    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
                    ]))
            except ValidationError :
                errors.append("密码太过简单")
    

    if len(errors) == 0:
        user = UserProfile.objects.create_user(password=password1,username=username)
        login(request,user)
        request.session['nickName']=user.get_nickName()
        return JsonResponse({})
    else:
        return JsonResponse({'logError':errors})
        

def userInfo(request,username):
    user = UserProfile.objects.filter(username=username).first()
    postList = Post.objects.all().filter(owner=user.id).order_by("-likesNum")
    return render(request,'userInfo.html',{'user':user,'postList':postList})

def modifyInfo(request):
    user = request.user
    user.nickName = request.POST.get("nickName")
    user.phone = request.POST.get("phone")
    user.qq = request.POST.get("qq")
    user.wechat = request.POST.get("wechat")
    user.sex = request.POST.get("sex")
    user.personalSignature = request.POST.get("personalSignature")
    if request.FILES.get('headPortrait'):
        user.headPortrait = request.FILES.get('headPortrait')
    user.save()

    return JsonResponse({})

def elimateSession(request,name):
    request.session[name] = ""
    return JsonResponse({})