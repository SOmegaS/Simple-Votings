from django.shortcuts import render

from simple_votings import database


def main_page(request):
    ctx = {}
    return render(request, 'main_page.html', ctx)
