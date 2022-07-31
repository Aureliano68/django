from django.contrib import admin
from .models import author,chief,publish,article

# Register your models here.

@admin.register(author)
class authorAdmin(admin.ModelAdmin):
    list_display=('name','family','age',)
    prepopulated_fields= {'slug':('name','family')}
    
    
@admin.register(chief)
class chiefAdmin(admin.ModelAdmin):
    list_display=('name','family')

@admin.register(publish)
class publishAdmin(admin.ModelAdmin):
    list_display=('name','chief')


@admin.register(article)
class articleAdmin(admin.ModelAdmin):
    list_display=('name_article','create_at','is_active','author')
    list_filter=('is_active',)
    search_fields=('ame_article',)
