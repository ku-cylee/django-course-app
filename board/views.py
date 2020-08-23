import math

from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest, HttpResponseNotFound

from .models import *
from .forms import *


def index(request):
    user = request.user if request.user.is_authenticated else None
    return render(request, 'index.html', {
        'user': user,
    })


def user_login(request):
    if request.method == 'GET':
        return login_form(request)
    if request.method == 'POST':
        return login_post(request)
    return HttpResponseNotFound()


def login_form(request):
    return render(request, 'auth/login.html', {
        'form': LoginForm(),
    })


def login_post(request):
    form = LoginForm(request.POST)
    if not form.is_valid():
        return HttpResponseBadRequest()
    
    user = authenticate(
        username=form.cleaned_data['username'],
        password=form.cleaned_data['password'],
    )
    login(request, user)
    return redirect('index')


def register(request):
    if request.method == 'GET':
        return register_form(request)
    if request.method == 'POST':
        return register_post(request)
    return HttpResponseNotFound()


def register_form(request):
    return render(request, 'auth/register.html', {
        'form': RegisterForm(),
    })


def register_post(request):
    form = RegisterForm(request.POST)
    if not form.is_valid():
        return HttpResponseBadRequest()

    User.objects.create_user(
        username=form.cleaned_data['username'],
        password=form.cleaned_data['password'],
        first_name=form.cleaned_data['first_name'],
        last_name=form.cleaned_data['last_name'],
    )
    return redirect('login')


def user_logout(request):
    logout(request)
    return redirect('index')


def get_article_list(request, page_num):
    COUNT = 20

    article_list = Article.objects.all().filter(is_deleted=False).order_by('-id')
    start_index = (page_num - 1) * COUNT
    end_index = page_num * COUNT

    page_count = math.ceil(len(article_list) / COUNT)

    return render(request, 'articles/index.html', {
        'page': page_num,
        'articles': article_list[start_index:end_index],
        'has_prev': page_num > 1,
        'has_next': page_num < page_count,
    })


def get_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if article.is_deleted:
        return HttpResponseNotFound()
        
    user = request.user if request.user.is_authenticated else None
    
    return render(request, 'articles/details.html', {
        'user': user,
        'article': article,
    })


def compose_article(request):
    if not request.user.is_authenticated:
        return HttpResponseNotFound()
    if request.method == 'GET':
        return compose_article_form(request)
    if request.method == 'POST':
        return compose_article_post(request)
    return HttpResponseNotFound()


def compose_article_form(request):
    return render(request, 'articles/compose.html', {
        'form': ArticleForm(),
    })


def compose_article_post(request):
    form = ArticleForm(request.POST)
    if not form.is_valid():
        return HttpResponseBadRequest()

    new_article = Article.objects.create(
        title=form.cleaned_data['title'],
        content=form.cleaned_data['content'],
        author=request.user,
    )
    new_article.save()

    return redirect('get_article', article_id=new_article.id)


def edit_article(request, article_id):
    if not request.user.is_authenticated:
        return HttpResponseNotFound()
    
    article = get_object_or_404(Article, id=article_id)
    if request.user != article.author or article.is_deleted:
        return HttpResponseNotFound()

    if request.method == 'GET':
        return edit_article_form(request, article)
    if request.method == 'POST':
        return edit_article_post(request, article)
    return HttpResponseNotFound()


def edit_article_form(request, article):
    return render(request, 'articles/compose.html', {
        'form': ArticleForm(initial={
            'title': article.title,
            'content': article.content,
        }),
    })


def edit_article_post(request, article):
    form = ArticleForm(request.POST)
    if not form.is_valid():
        return HttpResponseBadRequest()
    
    article.title = form.cleaned_data['title']
    article.content = form.cleaned_data['content']
    article.save()
    return redirect('get_article', article.id)


def delete_article(request, article_id):
    if not request.user.is_authenticated:
        return HttpResponseNotFound()
    
    article = get_object_or_404(Article, id=article_id)
    if request.user != article.author or article.is_deleted:
        return HttpResponseNotFound()

    article.is_deleted = True
    article.save()
    
    return redirect('article_list', page_num=1)
