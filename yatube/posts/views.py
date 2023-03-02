from django.conf import settings

from django.shortcuts import get_object_or_404, render

from .models import Group, Post

"""Главная страница."""


def index(request):
    posts = Post.objects.order_by('-pub_date')[:settings.POSTS_ON_PAGE]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


"""Страница с постами."""


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.order_by('-pub_date')[:settings.POSTS_ON_PAGE]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
