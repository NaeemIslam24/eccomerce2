from django.shortcuts import render
from . models import *

# Create your views here.
def blog(request):
    template = 'blog.html'
    post = Post.objects.all()


    context={

        'posts': post

    }

    return render(request, template_name=template, context=context)

def detail_blog(request, id, sl):
    template = 'blog-single.html'

    post = Post.objects.get(id = id, slug = sl)

    print('-------------------')
    print(post)
    context={
          'post': post
    }

    return render(request, template_name=template, context=context)