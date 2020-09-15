from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from posts.models import Post

# Create your views here.

@login_required
def follow_toggle(request, id):
    user = request.user
    profile = user.profile
    
    #게시글 쓴 사람
    followed_user = get_object_or_404(User, pk=id)

    #내가 팔로우 했는지 확인
    is_follower = profile in followed_user.profile.followers.all()

    if is_follower:
        profile.followings.remove(followed_user.profile)
        print("팔로우 취소")
    else:
        profile.followings.add(followed_user.profile)
        print("팔로우")
    return redirect('home')

def mypage(request, id):
    mypage_user = get_object_or_404(User, pk=id)
    context = {
        'posts' : Post.objects.filter(user=mypage_user),
        'followings' : mypage_user.profile.followings.all(),
        'followers' : mypage_user.profile.followers.all(),
    }
    return render(request, 'users/mypage.html', context)