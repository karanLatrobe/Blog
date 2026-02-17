
from django.shortcuts import render
from blog.models import Category , Blog


def home(request):
    category_list = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured = True).order_by('-updated_at')
    posts = Blog.objects.filter(is_featured = False).order_by('-updated_at')
    context = {
        'categories':category_list, 'featured_posts':featured_posts, 'posts':posts
    }
    return render(request,'home.html',context)