from django.contrib import admin
from .models import Programme

@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ['nom', 'jour', 'heure_debut', 'heure_fin', 'langue', 'animateur', 'actif']
    list_filter = ['jour', 'langue', 'actif']
    list_editable = ['actif']