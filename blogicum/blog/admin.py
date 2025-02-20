from django.contrib import admin
from .models import Category, Location, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    search_fields = ('title',)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'is_published')
    list_filter = ('is_published', 'category', 'location')
    search_fields = ('title', 'text')
    fieldsets = (
        (None, {
            'fields': (
                'title',
                'slug',
                'description',
                'text',
                'author',
                'category',
                'location',
                'pub_date',
                'is_published')
        }),
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)
