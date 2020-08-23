from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('articles/page/<int:page_num>/', views.articles, name='article_list'),
    path('article/<int:article_id>/', views.get_article, name='get_article'),
    path('article/compose/', views.compose_article, name='compose_article'),
    path('article/edit/<int:article_id/', views.edit_article, name='edit_article'),
    path('article/delete/<int:article_id>/', views.delete_article, name='delete_article'),
]
