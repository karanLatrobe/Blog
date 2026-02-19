
from django.shortcuts import render
from blog.models import Category , Blog


def home(request):
    featured_posts = Blog.objects.filter(is_featured = True, status = 'Publish').order_by('-created_at')
    posts = Blog.objects.filter(is_featured = False, status = 'Publish').order_by('-updated_at')
    context = {
        'featured_posts':featured_posts, 'posts':posts
    }
    return render(request,'home.html',context)

