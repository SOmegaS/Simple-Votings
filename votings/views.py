from django.shortcuts import render
from django.http import HttpRequest
from votings.database import database


def main_page(request: HttpRequest):
    ctx = {}
    return render(request, 'main_page.html', ctx)


def register_page(request: HttpRequest):
    ctx = {}
    return render(request, 'register_page.html', ctx)


def login_page(request: HttpRequest):
    ctx = {}
    return render(request, 'main_page.html', ctx)


def history_page(request: HttpRequest):
    ctx = {}
    return render(request, 'history_page.html', ctx)


def vote_page(request: HttpRequest):
    ctx = {}
    return render(request, 'vote_page.html', ctx)
