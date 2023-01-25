from django.shortcuts import render,redirect
from forum.models import Post

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
    postList = []
    menu = postType
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