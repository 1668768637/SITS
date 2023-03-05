from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout,password_validation
from django.core.exceptions import ValidationError
from .models import UserProfile
from forum.models import Post,userCollection,Message
from forum.views import findForumById
from django.http import JsonResponse
from string import ascii_letters,digits

@csrf_exempt
# Create your views here.
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
            user = authenticate(username=username, password=password)
            if user:
                logout(request)
                print(username+"||"+password)
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
        if len(username) > 10:
            errors.append("用户名太短")
        if UserProfile.objects.filter(username=username).exists():
            errors.append("用户名不唯一")
        for ch in username:
            if '\u4e00' <= ch <= '\u9fa5':
                errors.append("用户名不可以包含中文")
                break
        letterRange = ''.join(ascii_letters+digits)
        for ch in username:
            if ch not in letterRange:
                errors.append("含有非法字符："+ch)
                

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
    ua = request.META.get("HTTP_USER_AGENT")
    if judge_pc_or_mobile(ua):
        device = "mobile"
    else:
        device = "pc"
    if user:
        postList = Post.objects.all().filter(owner=user.id).order_by("-likesNum")
        collections = userCollection.objects.all().filter(userOwner=user)
        msgs = Message.objects.all().filter(receiver=user).order_by("create_date")
        return render(request,'userInfo.html',{'user':user,'postList':postList,"collections":collections,"device":device,"msgs":msgs})
    else:
        return render(request,'userInfo.html',{'user':user})

def modifyInfo(request):
    user = request.user
    if user.is_authenticated:
        user.nickName = request.POST.get("nickName")
        user.email = request.POST.get("email")
        user.phone = request.POST.get("phone")
        user.qq = request.POST.get("qq")
        user.wechat = request.POST.get("wechat")
        user.sex = request.POST.get("sex")
        if request.POST.get("password") != "":
            modifyPassword(request,request.POST.get("password"))
        user.personalSignature = request.POST.get("personalSignature")
        if request.FILES.get('headPortrait') and user.headPortrait != request.FILES.get('headPortrait'):
            user.headPortrait.delete(False)
            user.headPortrait = request.FILES.get('headPortrait')
        user.save()

        return JsonResponse({})
    else:
        return JsonResponse({"errors":"非法警告"})

def modifyPassword(request,password):
    if request.user.is_authenticated:
        request.user.set_password(password)
        request.user.save()
    return JsonResponse({})

def forgetPassword(request,username):
    user = UserProfile.objects.all().filter(username=username).first()
    if user:
        user.set_password("123456")
        user.save()
    return JsonResponse({})

def delUser(request):
    if request.user.is_authenticated:
        user = request.user
        logout(request)
        user.delete()
        return JsonResponse({})
    else:
        return JsonResponse({"errors":"非法警告"})
    

def readMessage(request,msgId):
    msg = Message.objects.all().filter(id=msgId).first()
    if msg:
        msg.read()
        return findForumById(request,msg.post.id)
    else:
        return JsonResponse({'errors':"无效的消息内容!"})

# 判断访问来源是pc端还是手机端
import re

def judge_pc_or_mobile(ua):
    """
    :param ua: 访问来源头信息中的User-Agent字段内容
    :return:
    """

    factor = ua
    is_mobile = False

    _long_matches = r'googlebot-mobile|android|avantgo|blackberry|blazer|elaine|hiptop|ip(hone|od)|kindle|midp|mmp' \
                    r'|mobile|o2|opera mini|palm( os)?|pda|plucker|pocket|psp|smartphone|symbian|treo|up\.(browser|link)' \
                    r'|vodafone|wap|windows ce; (iemobile|ppc)|xiino|maemo|fennec'
    _long_matches = re.compile(_long_matches, re.IGNORECASE)
    _short_matches = r'1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)' \
                     r'|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)' \
                     r'|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw' \
                     r'|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8' \
                     r'|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit' \
                     r'|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)' \
                     r'|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji' \
                     r'|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|e\-|e\/|\-[a-w])|libw|lynx' \
                     r'|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(di|rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi' \
                     r'|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)' \
                     r'|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg' \
                     r'|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21' \
                     r'|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-' \
                     r'|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it' \
                     r'|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)' \
                     r'|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)' \
                     r'|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit' \
                     r'|wi(g |nc|nw)|wmlb|wonu|x700|xda(\-|2|g)|yas\-|your|zeto|zte\-'

    _short_matches = re.compile(_short_matches, re.IGNORECASE)

    if _long_matches.search(factor) != None:
        is_mobile = True
    user_agent = factor[0:4]
    if _short_matches.search(user_agent) != None:
        is_mobile = True

    return is_mobile