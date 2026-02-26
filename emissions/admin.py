from django.contrib import admin
from .models import Emission, TypeEmission

@admin.register(TypeEmission)
class TypeEmissionAdmin(admin.ModelAdmin):
    list_display = ['nom', 'icone', 'slug']
    prepopulated_fields = {'slug': ('nom',)}

@admin.register(Emission)
class EmissionAdmin(admin.ModelAdmin):
    list_display = ['titre', 'type_emission', 'animateur', 'date_diffusion', 'langue', 'publie', 'nb_ecoutes']
    list_filter = ['type_emission', 'langue', 'publie', 'date_diffusion']
    search_fields = ['titre', 'description']
    list_editable = ['publie']
    date_hierarchy = 'date_diffusion'