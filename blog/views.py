from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog, Category
from django.db.models import Q
# Create your views here.

def post_by_category(request,category_id):
    posts = Blog.objects.filter(category_id = category_id, status = "Publish", is_featured = True)

    try:
        category = Category.objects.get(pk = category_id)
    except:
        return redirect("home")
    
    context = {
        "posts":posts,"category":category
    }
    return render(request, "category_post.html",context)



def blogs(request,slug):
    single_blog = get_object_or_404(Blog,slug = slug)
    context ={
        'single_blog':single_blog
    }
    return render(request,'single_blog.html',context)



def search(request):
    keyword = request.GET.get('keyword')
    blog = Blog.objects.filter(Q(title__icontains = keyword) |Q(short_description__icontains = keyword) |Q(blog_body__icontains = keyword) )

    context = {
        "blogs" : blog,"keyword":keyword
    }
    return render(request,"article.html",context)
    