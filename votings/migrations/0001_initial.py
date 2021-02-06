# Generated by Django 3.1.4 on 2021-02-04 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.TextField()),
                ('passwd', models.TextField()),
                ('role', models.IntegerField()),
                ('polls_create', models.TextField()),
                ('polls_voted', models.TextField()),
                ('photo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Votings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField()),
                ('name', models.TextField()),
                ('variants', models.TextField()),
                ('choose_type', models.TextField()),
                ('color', models.TextField()),
                ('back_ground_image', models.TextField()),
            ],
        ),
    ]