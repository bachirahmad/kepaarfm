from django.contrib import admin
from .models import Animateur

@admin.register(Animateur)
class AnimateurAdmin(admin.ModelAdmin):
    list_display = ['nom', 'role', 'emission_principale', 'actif', 'ordre']
    list_editable = ['actif', 'ordre']
    search_fields = ['nom', 'role']