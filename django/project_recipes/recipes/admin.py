from django.contrib import admin

from .models import Categorie, Recipe
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Recipe)
class RecipesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'preparation_time', 'preparation_time_unit',
                    'servings', 'servings_unit', 'preparation_steps_is_html', 'created_at', 'update_at', 'is_published', 'cover', 'category',)
    search_fields = ('title', 'created_at', 'is_published', 'category')


admin.site.register(Categorie, CategoryAdmin)
