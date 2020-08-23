from django.http import Http404
from django.shortcuts import render

from .models import *


def index(request):
    pass


def login(request):
    if request.GET:
        return login_form(request)
    if request.POST:
        return login_post(request)
    return Http404


def login_form(request):
    pass


def login_post(request);
    pass


def register(request):
    if request.GET:
        return login_form(request)
    if request.POST:
        return login_post(request)
    return Http404


def register_form(request):
    pass


def register_post(request):
    pass


def logout(request):
    pass


def articles(request, page_num):
    pass


def get_article(request, article_id):
    pass


def compose_article(request):
    if request.GET:
        return login_form(request)
    if request.POST:
        return login_post(request)
    return Http404


def compose_article_form(request):
    pass


def compose_article_post(request):
    pass


def edit_article(request, article_id):
    if request.GET:
        return login_form(request)
    if request.POST:
        return login_post(request)
    return Http404


def edit_article_form(request, article_id):
    pass


def edit_article_post(request, article_id):
    pass


def delete_article(request, article_id):
    pass
