from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Company(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название компании")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    website = models.URLField(blank=True, null=True, verbose_name="Веб-сайт")
    # logo = models.ImageField(upload_to='company_logos/', blank=True, null=True, verbose_name="Логотип") # Requires Pillow and media setup

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

class Vacancy(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название вакансии")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies', verbose_name="Компания")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='vacancies', verbose_name="Категория")
    description = models.TextField(verbose_name="Описание вакансии")
    requirements = models.TextField(blank=True, null=True, verbose_name="Требования")
    salary_from = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Зарплата от")
    salary_to = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Зарплата до")
    currency = models.CharField(max_length=10, blank=True, null=True, verbose_name="Валюта")
    location = models.CharField(max_length=100, verbose_name="Местоположение")
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    is_active = models.BooleanField(default=True, verbose_name="Активна")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
        ordering = ['-published_date']

