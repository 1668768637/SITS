from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from forum.models import Post
from django.http import JsonResponse
from django.core.paginator import Paginator
from user.models import UserProfile
from django.db.models import Q
@csrf_exempt

# Create your views here.
def home(request):
    postList = Post.objects.all().filter(isChecked=True).order_by("-publishDate")
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
    return render(request,'home.html',{'active_menu':'home','postList':postList,'pageData': pageData,})

def search(request):
    info = request.GET['info']
    if info:
        userList = UserProfile.objects.all().filter(Q(username__icontains=info) | Q(nickName__icontains=info))

        return render(request,'result.html',{'userList':userList,})
    else:
        return render(request,'result.html',{'userList':None,})
