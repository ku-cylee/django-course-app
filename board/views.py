from django.shortcuts import render, redirect
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


def articles(request, page_num):
    pass


def get_article(request, article_id):
    pass


def compose_article(request):
    if request.method == 'GET':
        return compose_article_form(request)
    if request.method == 'POST':
        return compose_article_post(request)
    return HttpResponseNotFound()


def compose_article_form(request):
    pass


def compose_article_post(request):
    pass


def edit_article(request, article_id):
    if request.method == 'GET':
        return edit_article_form(request)
    if request.method == 'POST':
        return edit_article_post(request)
    return HttpResponseNotFound()


def edit_article_form(request, article_id):
    pass


def edit_article_post(request, article_id):
    pass


def delete_article(request, article_id):
    pass
