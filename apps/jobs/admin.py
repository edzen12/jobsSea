from django.contrib import admin
from .models import Category, Company, Vacancy

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')
    search_fields = ('name',)

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'category', 'location', 'published_date', 'is_active')
    list_filter = ('is_active', 'category', 'company', 'location')
    search_fields = ('title', 'company__name', 'description', 'requirements')
    date_hierarchy = 'published_date'
    ordering = ('-published_date',)
    fieldsets = (
        (None, {
            'fields': ('title', 'company', 'category', 'location')
        }),
        ('Детали вакансии', {
            'fields': ('description', 'requirements')
        }),
        ('Зарплата', {
            'fields': (('salary_from', 'salary_to'), 'currency')
        }),
        ('Статус', {
            'fields': ('is_active',)
        }),
    )
    # readonly_fields = ('published_date',)

