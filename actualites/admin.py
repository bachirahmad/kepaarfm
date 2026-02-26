from django.contrib import admin
from .models import Actualite

@admin.register(Actualite)
class ActualiteAdmin(admin.ModelAdmin):
    list_display = ['titre', 'categorie', 'publie', 'en_une', 'created_at']
    list_filter = ['categorie', 'publie', 'en_une']
    search_fields = ['titre', 'contenu']
    list_editable = ['publie', 'en_une']
    prepopulated_fields = {'slug': ('titre',)}