from django.shortcuts import render,redirect,get_object_or_404
from blog.models import Category, Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, BlogForm
from django.utils.text import slugify

@login_required(login_url='login')
def dashboard(request):
    Categories = Category.objects.all().count()
    article = Blog.objects.all().count()

    context= {
        'total_categories':Categories,
        'total_articles': article
    }
    return render(request,'dashboard/dashboard.html',context)


@login_required(login_url='login')
def dashboard_categories(request):
    Categories = Category.objects.all()
    context  = {
        'total_categories':Categories,
    }
    return render(request, 'dashboard/dashboard_categories.html',context)


def add_category(request):

    if request.method == "POST":
        form = CategoryForm(request.POST)
        
        if form.is_valid():
            form.save()
            redirect('dashboard_categories')
    else:
        form = CategoryForm()

    context = {'form':form,}
    return render(request, "dashboard/add_category.html",context)



def edit_category(request,pk):
    category = get_object_or_404(Category, pk = pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance = category)
        if form.is_valid():
            form.save()
            return redirect("dashboard_categories")
    else:
        form = CategoryForm(instance = category)
    context = {'form':form, 'category':category}
    return render(request, "dashboard/edit_category.html",context)



def delete_category(request,pk):
    category = get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect("dashboard_categories")


def dashboard_article(request):
    articles = Blog.objects.all()
    context = {'articles':articles}
    return render(request,'dashboard/dashboard_article.html', context)


def article_add(request):
    if request.method == "POST":
        form  = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            form_temp = form.save(commit=False)
            form_temp.author = request.user
            form.save()
            return redirect("dashboard_article")
    else:
        form = BlogForm()
    context = {
        'form':form
    }
    return render(request, 'dashboard/article_add.html', context)