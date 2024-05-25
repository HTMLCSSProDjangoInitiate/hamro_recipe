from django.contrib import admin
from .models import Recipe, delivery

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    search_fields = ['title', 'user__username']
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)

admin.site.register(Recipe, RecipeAdmin)

admin.site.register(delivery)