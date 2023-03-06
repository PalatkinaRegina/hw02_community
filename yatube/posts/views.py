from django.core.paginator import Paginator
from django.conf import settings
from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request):
    """Главная страница."""
    posts = Post.objects.order_by('-pub_date')[:settings.POSTS_ON_PAGE]
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    """Страница с постами."""
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.order_by('-pub_date')[:settings.POSTS_ON_PAGE]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
