from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from django.contrib.auth import get_user_model

User = get_user_model()

from .models import Post


def post_list(request):
    #전부 다가져올때
    # posts = Post.objects.all()

    #조건 오늘날짜로부터 이전날짜를 검색
    # posts = Post.objects.filter(published_date__lte=timezone.now())

    #posts 변수에 전체 Post를 최신내림차순으로 정렬할 쿼리셋을 대입
    posts = Post.objects.order_by('-created_date')
    context = {
        'title':'PostList from post_list view',
        'posts':posts,
    }
    return render(request, 'blog/post_list.html',context=context)



def post_detail(request,pk):
    # post라는 키값으로 pk또는 id값이 매개변수로 주어진 pk변수와 같은 post객체를 전달
    context = {
        'post': Post.objects.get(pk=pk),
    }

    return render(request, 'blog/post_detail.html', context)

def post_create(request):
    if request.method == 'GET':
        context = {


        }
        return render(request, 'blog/post_create.html', context)
    elif request.method == 'POST':
        data = request.POST
        print(data)
        title = data['title']
        text = data['text']
        user = User.objects.first()
        post = Post.objects.create(
            title=title,
            text=text,
            author=user
        )
        return redirect('post_detail',pk=post.pk)
