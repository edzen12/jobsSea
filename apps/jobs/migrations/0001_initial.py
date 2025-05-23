# Generated by Django 5.2.1 on 2025-05-14 11:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название компании')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Веб-сайт')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название вакансии')),
                ('description', models.TextField(verbose_name='Описание вакансии')),
                ('requirements', models.TextField(blank=True, null=True, verbose_name='Требования')),
                ('salary_from', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Зарплата от')),
                ('salary_to', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Зарплата до')),
                ('currency', models.CharField(blank=True, max_length=10, null=True, verbose_name='Валюта')),
                ('location', models.CharField(max_length=100, verbose_name='Местоположение')),
                ('published_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активна')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vacancies', to='jobs.category', verbose_name='Категория')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='jobs.company', verbose_name='Компания')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
                'ordering': ['-published_date'],
            },
        ),
    ]
