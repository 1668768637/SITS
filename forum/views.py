from django.shortcuts import render,redirect
from forum.models import Post,PostImage,PostLike,Commit,userCollection,Message
from django.http import JsonResponse
from django.core.paginator import Paginator
# Create your views here.

def forum(request,postType):
    menu = postType
    postList = []
    if postType == "anecdoteForum":
        postList = Post.objects.all().filter(postType="anecdoteForum",isChecked=True).order_by("-publishDate")
        postType = "校园轶事"
    if postType == "lostAndFound":
        postList = Post.objects.all().filter(postType="lostAndFound",isChecked=True).order_by("-publishDate")
        postType = "失物招领"
    if postType == "driftBottle":
        postList = Post.objects.all().filter(postType="driftBottle",isChecked=True).order_by("-publishDate")
        postType = "漂流瓶"
    if postType == "eventInformation":
        postList = Post.objects.all().filter(postType="eventInformation",isChecked=True).order_by("-publishDate")
        postType = "活动信息"
    if postType == "loveWall":
        postList = Post.objects.all().filter(postType="loveWall",isChecked=True).order_by("-publishDate")
        postType = "表白墙"

    p = Paginator(postList,10)
    if p.num_pages <= 1:
        pageData = ''
    else:
        page = int(request.GET.get('page', 1))
        postList = p.page(page)
        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        total_pages = p.num_pages
        page_range = p.page_range
        if page == 1:
            right = page_range[page:page + 2]
            print(total_pages)
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page == total_pages:
            left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
            left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]
            right = page_range[page:page + 2]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        pageData = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
            'total_pages': total_pages,
            'page': page,
        }

    return render(request,'forum.html',{'active_menu':menu,'postList':postList,'postType':postType,'pageData': pageData})

def findForumById(request,postId):
    post = Post.objects.all().filter(id=postId)
    return render(request,'postDetail.html',{'post':post[0],})

#新建帖子
def newPost(request):
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
            postLike = PostLike.objects.create(user=request.user,post=post,)
            postLike.save()
            post.likesNum = post.likesNum+1
            post.save()
            msg = Message.objects.create(poster=request.user,
                                         receiver=post.owner,
                                         post=post,
                                         context="点赞了你的帖子")
            msg.save()
            return JsonResponse({'state':'success','id':postId})
        else:
            return JsonResponse({'state':'fail','error':'您已经点过赞了'})
    else:
        return JsonResponse({'state':'fail','error':'您还没有登录'})

#删除帖子
def delPost(request,postId):
    post = Post.objects.all().filter(id=postId).first()
    if post:
        if request.user == post.owner:
            post.delete(False)
            return JsonResponse({})
        else:
            return JsonResponse({"errors":"不能删除他人的帖子！！！"})
    else:
        return JsonResponse({"errors":"帖子不存在！"})

#评论
#需要在request中提供对应的owner，context和id
def commit(request):
    owner = request.POST.get("owner")
    id = request.POST.get("id")
    errors = []
    if request.user.is_authenticated:
        context = request.POST.get("context")
        if context:
            if owner == "post":
                post = Post.objects.all().filter(id=id).first()
                if Commit.objects.all().filter(postOwner = post,context=context,userOwner=request.user).exists():
                    errors.append("评论重复")
                else:
                    commit = Commit(postOwner = post,context=context,userOwner=request.user)
                    commit.save()
                    msg = Message.objects.create(poster=request.user,
                                                receiver=post.owner,
                                                post=post,
                                                context="评论了你的帖子")
                    msg.save()
            elif owner == "commit":
                commitOwner = Commit.objects.all().filter(id=id).first()
                if Commit.objects.all().filter(commitOwner = commitOwner,context=context,userOwner=request.user).exists():
                    errors.append("评论重复")
                else:
                    commit = Commit(commitOwner = commitOwner,context=context,userOwner=request.user)
                    commit.save()
                    msg1 = Message.objects.create(poster=request.user,
                                                receiver=commitOwner.userOwner,
                                                post=commitOwner.postOwner,
                                                context="评论了你的发言")
                    msg1.save()


                    msg2 = Message.objects.create(poster=request.user,
                                                receiver=commitOwner.postOwner.owner,
                                                post=commitOwner.postOwner,
                                                context="评论了你的帖子")
                    msg2.save()
        else:
            errors.append("评论不能是空的")
    else:
        errors.append("您还没有登录")
    return JsonResponse({'id':id,'owner':owner,'errors':errors})

def delCommit(request,id):
    if request.user.is_authenticated:
        commit = Commit.objects.all().filter(id=id).first()
        if commit and request.user==commit.userOwner:
            commit.delete()
            return JsonResponse({})
        else:
            return JsonResponse({"errors":"不能删除他人帖子"})
    else:
        return JsonResponse({"errors":"非法警告"})

def makeCollection(request,postId):
    if request.user.is_authenticated:
        post = Post.objects.all().filter(id=postId).first()
        if not userCollection.objects.filter(userOwner=request.user,postOwner=post).exists():
            UC = userCollection.objects.create(userOwner=request.user,postOwner=post)
            if UC:
                UC.save()
                return JsonResponse({})
            else:
                return JsonResponse({"errors":"未知错误，收藏失败"})
        else:
            return JsonResponse({"errors":"您已经收藏过了"})
    return JsonResponse({"errors":"用户未登录"})


def delCollection(request,collectionId):
    colt = userCollection.objects.filter(id=collectionId).first()
    if colt and request.user==colt.userOwner:
        colt.delete()
        return JsonResponse({})
    else:
        return JsonResponse({"errors":"删除失败"})