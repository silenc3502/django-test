from django.shortcuts import render

# Create your views here.
from .models import Post

def index(request):
    # order_by를 통해 최신 컨텐츠부터 보여준다.
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'blog/index.html',
        {
            'posts': posts
        }
    )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post': post,
        }
    )