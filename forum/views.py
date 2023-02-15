from django.shortcuts import render,redirect
from forum.models import Post,PostImage,PostLike,Commit
from django.http import JsonResponse

# Create your views here.

def forum(request,postType):
    menu = postType
    postList = []
    if postType == "anecdoteForum":
        postList = Post.objects.all().filter(postType="anecdoteForum").order_by("-likesNum")[:4]
        postType = "校园轶事"
    if postType == "lostAndFound":
        postList = Post.objects.all().filter(postType="lostAndFound").order_by("-likesNum")[:4]
        postType = "失物招领"
    if postType == "driftBottle":
        postList = Post.objects.all().filter(postType="driftBottle").order_by("-likesNum")[:4]
        postType = "漂流瓶"
    if postType == "eventInformation":
        postList = Post.objects.all().filter(postType="eventInformation").order_by("-likesNum")[:4]
        postType = "活动信息"
    if postType == "loveWall":
        postList = Post.objects.all().filter(postType="loveWall").order_by("-likesNum")[:4]
        postType = "表白墙"
    return render(request,'forum.html',{'active_menu':menu,'postList':postList,'postType':postType})

def findForumById(request,postId):
    post = Post.objects.all().filter(id=postId)
    return render(request,'postDetail.html',{'post':post[0],})

#新建帖子
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
        return JsonResponse({'postErrors':errors})

#点赞帖子
def likePost(request,postId):
    if request.user.is_authenticated:
        post = Post.objects.all().filter(id=postId).first()
        if(not PostLike.objects.all().filter(user=request.user,post=post).exists()):
            postLike = PostLike.objects.create(user=request.user,post=post)
            postLike.save()
            post.likesNum = post.likesNum+1
            post.save()
            return JsonResponse({'state':'success','id':postId})
        else:
            return JsonResponse({'state':'fail','error':'您已经点过赞了'})
    else:
        return JsonResponse({'state':'fail','error':'您还没有登录'})

#删除帖子
def delPost(request,postId):
    post = Post.objects.all().filter(id=postId).first()
    post.delete()
    return JsonResponse({})

#评论
#需要在request中提供对应的owner，context和id
def commit(request):
    owner = request.POST.get("owner")
    id = request.POST.get("id")
    context = request.POST.get("context")
    if owner == "post":
        post = Post.objects.all().filter(id=id).first()
        commit = Commit(postOwner = post,context=context)
        commit.userOwner = request.user
        commit.save()
    else:
        commitOwner = Commit.objects.all().filter(id=id).first()
        commit = Commit(commitOwner = commitOwner,context=context)
        commit.userOwner = request.user
        commit.save()
    return JsonResponse({})