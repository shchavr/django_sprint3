
from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.utils import timezone


def published(post_objects):
    return post_objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )


def index(request):
    template_name = 'blog/index.html'
    post_list = published(Post.objects).order_by('-pub_date')[:5]
    context = {'post_list': post_list}
    return render(request, template_name, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    posts = get_object_or_404(published(Post.objects), id=id)
    context = {
        'post': posts
    }
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(Category,
                                 slug=category_slug, is_published=True)

    post_list = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now()
    )

    context = {
        'category': category,
        'post_list': post_list
    }

    return render(request, template, context)
