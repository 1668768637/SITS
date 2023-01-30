from django.shortcuts import render,redirect
from forum.models import Post,PostImage
from django.http import JsonResponse

# Create your views here.

def anecdoteForum(request):
    postList = Post.objects.all().filter(postType="anecdoteForum").order_by("likesNum")
    return render(request,'anecdoteForum.html',{'active_menu':'anecdoteForum','postList':postList})

def lostAndFound(request):
    return render(request,'lostAndFound.html',{'active_menu':'lostAndFound'})

def driftBottle(request):
    return render(request,'driftBottle.html',{'active_menu':'driftBottle'})

def eventInformation(request):
    return render(request,'eventInformation.html',{'active_menu':'eventInformation'})
    
def loveWall(request):
    return render(request,'loveWall.html',{'active_menu':'loveWall'})

def forum(request,postType):
    menu = postType
    postList = []
    if postType == "anecdoteForum":
        postList = Post.objects.all().filter(postType="anecdoteForum").order_by("likesNum")
        postType = "校园轶事"
    if postType == "lostAndFound":
        postList = Post.objects.all().filter(postType="lostAndFound").order_by("likesNum")
        postType = "失物招领"
    if postType == "driftBottle":
        postList = Post.objects.all().filter(postType="driftBottle").order_by("likesNum")
        postType = "漂流瓶"
    if postType == "eventInformation":
        postList = Post.objects.all().filter(postType="eventInformation").order_by("likesNum")
        postType = "活动信息"
    if postType == "loveWall":
        postList = Post.objects.all().filter(postType="loveWall").order_by("likesNum")
        postType = "表白墙"
    return render(request,'forum.html',{'active_menu':menu,'postList':postList,'postType':postType})

def findForumById(request,postId):
    post = Post.objects.all().filter(id=postId)
    return render(request,'postDetail.html',{'post':post[0],})

def test(request):
    post = Post(id=1)
    postImg = PostImage(owner=post.id,photo="")
    return 

def newPost(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            sourceHtml = request.META['HTTP_REFERER']
            request.session['userError'] = "必须登录才能新建帖子"
            return redirect(sourceHtml)

        return render(request,'newPost.html')
    else:
        if request.method == 'POST':
            errors = []
            title=request.POST.get("title")
            context=request.POST.get("context")
            if title=="" or context=="":
                errors.append("标题和内容不能为空")
            else:
                post = Post(
                    title=request.POST.get("title"),
                    context=request.POST.get("context"),
                    owner=request.user,
                    postType=request.POST.get("postType"),
                    )
                print(post)
                post.save()
                imgs = request.FILES.getlist('postImages')
                for i in imgs:
                    img = PostImage(owner=post,photo=i)
                    if img:
                        img.save()
                    else:
                        errors.append(i.name+'上传失败')
        return render(request,'newPost.html',{'postErrors':errors})

def likePost(request,postId):
    post = Post.objects.all().filter(id=postId).first()
    post.likesNum = post.likesNum+1
    post.save()
    return JsonResponse({})