from django.shortcuts import render,redirect
from .models import Blog, Category
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