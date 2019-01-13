from django.contrib import admin
from rango_app.models import Category, Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category','url')

# Add in this class to include this customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)