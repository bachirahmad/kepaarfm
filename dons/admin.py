from django.contrib import admin
from .models import Don

@admin.register(Don)
class DonAdmin(admin.ModelAdmin):
    list_display = ['nom_donateur', 'montant', 'methode', 'statut', 'created_at']
    list_filter = ['methode', 'statut']
    search_fields = ['nom_donateur', 'telephone', 'reference']
    readonly_fields = ['created_at']