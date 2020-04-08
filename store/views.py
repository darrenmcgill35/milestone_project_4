from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from blog.models import Post
from .models import Store


@login_required
def all_stores(request):
    stores = Store.objects.all()
    posts = Post.objects.all()

    return render(request, 'store/store.html', {"stores": stores, "posts": posts})
