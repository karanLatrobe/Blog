from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard, name = 'dashboard'),

    # ==================== Categories==========================
    path('categories/',views.dashboard_categories, name = 'dashboard_categories'),
    path('categories/add/',views.add_category, name = "add_category"),
    path('categories/edit/<int:pk>/',views.edit_category , name = "edit_category"),
    path('categories/delete/<int:pk>/',views.delete_category , name = "delete_category"),

    # ==================== Articles ======================
    path('article/',views.dashboard_article , name = 'dashboard_article'),
    path('article/add',views.article_add, name = 'article_add')
]