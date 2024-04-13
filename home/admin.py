from django.contrib import admin
from . import models
from .models import Category, Post


@admin.register(models.ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created', 'read']
    list_filter = ['read', 'created']
    search_fields = ['name', 'email', 'subject', 'message']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(models.PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')  # Fields to display in the list view
    list_filter = ('title', 'date')  # Replace 'category' with actual fields
    search_fields = ('title', 'description')  # Fields to search in the admin panel
    date_hierarchy = 'date'  # Add date-based navigation to the admin panel

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')  # Define which fields to display in the admin list view
    search_fields = ('title', 'description')  # Add fields for searching

