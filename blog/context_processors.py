
from .models import Category 
from assignments.models import About , Social_Media_Links

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories = categories)


def About_detail(request):
    try:
        about = About.objects.get()
    except:
        about = None
    return dict(about = about)


def Social_links(request):
    try:
        social_links = Social_Media_Links.objects.all()
    except:
        social_links = None 
    return dict(social_links = social_links)