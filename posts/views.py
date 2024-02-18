from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Post, Group
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .forms import PostCreationForm



def index(request):
    post = Post.objects.order_by('-pub_date')[:10]
    paginator = Paginator(post, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': page_obj
    }
    return render(request, 'posts/index.html', context)

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    user = User.objects.get(username=username)
    context = {
        'user':user
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)    
    context = {
        'post':post
    }
    return render(request, 'posts/post_detail.html', context) 


def post_create(request):
    form = PostCreationForm()
    if request.method == 'POST':
        form = PostCreationForm()
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('posts:index'))
        return render(request, 'posts/create_post.html', {'form':form})
    return render(request,'posts/create_post.html', {'form':form})
