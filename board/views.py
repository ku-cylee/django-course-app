import math

from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponse

from .models import *
from .forms import *


def index(req):
    return render(req, 'index.html')


def user_login(req):
    if req.user.is_authenticated:
        return HttpResponse(status=404)
    if req.method == 'GET':
        return login_form(req)
    if req.method == 'POST':
        return login_post(req)
    return HttpResponse(status=404)


def login_form(req):
    return render(req, 'auth/login.html', {
        'form': LoginForm(),
    })


def login_post(req):
    form = LoginForm(req.POST)
    if not form.is_valid():
        return HttpResponse(status=400)
    
    user = authenticate(
        username=form.cleaned_data['username'],
        password=form.cleaned_data['password'],
    )

    if user:
        login(req, user)
        return redirect('index')
    else:
        return HttpResponse(status=401)


def register(req):
    if req.user.is_authenticated:
        return HttpResponse(status=404)
    if req.method == 'GET':
        return register_form(req)
    if req.method == 'POST':
        return register_post(req)
    return HttpResponse(status=404)


def register_form(req):
    return render(req, 'auth/register.html', {
        'form': RegisterForm(),
    })


def register_post(req):
    form = RegisterForm(req.POST)
    if not form.is_valid():
        return HttpResponse(status=400)

    user = User.objects.create_user(
        username=form.cleaned_data['username'],
        password=form.cleaned_data['password'],
        first_name=form.cleaned_data['first_name'],
        last_name=form.cleaned_data['last_name'],
    )
    user.save()
    return redirect('login')


def user_logout(req):
    logout(req)
    return redirect('index')


def get_article_list(req, page_num):
    COUNT = 20

    article_list = Article.objects.all().filter(is_deleted=False).order_by('-id')
    start_index = (page_num - 1) * COUNT
    end_index = page_num * COUNT

    page_count = math.ceil(len(article_list) / COUNT)

    return render(req, 'articles/index.html', {
        'page': page_num,
        'articles': article_list[start_index:end_index],
        'has_prev': page_num > 1,
        'has_next': page_num < page_count,
    })


def get_article(req, article_id):
    article = get_object_or_404(Article, id=article_id, is_deleted=False)
        
    return render(req, 'articles/details.html', {
        'article': article,
    })


def compose_article(req):
    if not req.user.is_authenticated:
        return HttpResponse(status=404)
    if req.method == 'GET':
        return compose_article_form(req)
    if req.method == 'POST':
        return compose_article_post(req)
    return HttpResponse(status=404)


def compose_article_form(req):
    return render(req, 'articles/compose.html', {
        'form': ArticleForm(),
    })


def compose_article_post(req):
    form = ArticleForm(req.POST)
    if not form.is_valid():
        return HttpResponse(status=400)

    new_article = Article.objects.create(
        title=form.cleaned_data['title'],
        content=form.cleaned_data['content'],
        author=req.user,
    )
    new_article.save()

    return redirect('get_article', article_id=new_article.id)


def edit_article(req, article_id):
    if not req.user.is_authenticated:
        return HttpResponse(status=404)
    
    article = get_object_or_404(Article, 
                    id=article_id, is_deleted=False, author=req.user)

    if req.method == 'GET':
        return edit_article_form(req, article)
    if req.method == 'POST':
        return edit_article_post(req, article)
    return HttpResponse(status=404)


def edit_article_form(req, article):
    return render(req, 'articles/compose.html', {
        'form': ArticleForm(initial={
            'title': article.title,
            'content': article.content,
        }),
    })


def edit_article_post(req, article):
    form = ArticleForm(req.POST)
    if not form.is_valid():
        return HttpResponse(status=400)
    
    article.title = form.cleaned_data['title']
    article.content = form.cleaned_data['content']
    article.save()
    return redirect('get_article', article.id)


def delete_article(req, article_id):
    if not req.user.is_authenticated:
        return HttpResponse(status=404)
    
    article = get_object_or_404(Article, 
                    id=article_id, is_deleted=False, author=req.user)

    article.is_deleted = True
    article.save()
    
    return redirect('article_list', page_num=1)
