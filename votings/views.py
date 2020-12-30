from django.shortcuts import render

from votings.database import database


def main_page(request):
    ctx = {}
    return render(request, 'main_page.html', ctx)
