from django.contrib import admin
from django.urls import path

from votings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page),
    path('register/', views.register_page),
    path('login/', views.login_page),
    path('poll/', views.vote_page),
    path('history/', views.history_page),
    path('profile/', views.profile_page),
]
