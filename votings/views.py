from django.shortcuts import render
from django.http import HttpRequest

from votings.models import Users, Votings


def main_page(request: HttpRequest):
    ctx = {}
    return render(request, 'votings/index.html', ctx)


def register_page(request: HttpRequest):
    ctx = {}
    return render(request, 'votings/register.html', ctx)


def login_page(request: HttpRequest):
    ctx = {}
    return render(request, 'votings/login.html', ctx)


def history_page(request: HttpRequest):
    ctx = {}
    return render(request, 'votings/history_page.html', ctx)


def vote_page(request: HttpRequest):
    ctx = {}
    return render(request, 'votings/poll.html', ctx)

def profile_page(request: HttpRequest):
    ctx = {}
    return render(request, 'votings/profile.html', ctx)
