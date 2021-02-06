from django.contrib import admin
from django.urls import path

from votings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page, name='index'),
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('poll/', views.vote_page, name='poll'),
    path('history/', views.history_page, name='history'),
    path('profile/', views.profile_page, name='profile'),
    path('votings/', views.votings_page, name='votings'),
    path('themes/', views.themes_page, name='themes'),
    path('create/', views.create_poll_page, name='create'),
]
