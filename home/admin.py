from django.contrib import admin
from .models import Category, JobListing

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'color_code', 'icon', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('is_active',)
    date_hierarchy = 'created_at'


@admin.register(JobListing)
class JobListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location_state', 'featured', 'is_active', 'created_at')
    list_filter = ('featured', 'is_active', 'category', 'location_state')
    search_fields = ('title', 'description')
    list_editable = ('featured', 'is_active')