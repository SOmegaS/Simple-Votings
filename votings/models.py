from django.db import models


class Users(models.Model):
    name = models.TextField()  # Имя
    email = models.TextField()  # E-mail
    passwd = models.TextField()  # Пароль
    role = models.IntegerField()  # Роль (0 - обычный, 1 - админ)
    polls_create = models.TextField()  # Созданные пользователем голосования
    polls_voted = models.TextField()  # ???
    photo = models.TextField()  # Путь к фото профиля


class Votings(models.Model):
    type = models.TextField()  # Тип чего???
    name = models.TextField()  # Имя
    variants = models.TextField()  # Варианты ответов
    choose_type = models.TextField()  # ???
    color = models.TextField()  # Цвет
    back_ground_image = models.TextField()  # Фоновая картинка
