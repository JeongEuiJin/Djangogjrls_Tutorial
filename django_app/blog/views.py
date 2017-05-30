from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from .models import Post


def post_list(request):
    #전부 다가져올때
    posts = Post.objects.all()

    #조건 오늘날짜로부터 이전날짜를 검색
    # posts = Post.objects.filter(published_date__lte=timezone.now())
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