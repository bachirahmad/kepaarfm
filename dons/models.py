from django.db import models # type: ignore

class Don(models.Model):
    METHODE_CHOICES = [
        ('wave', 'Wave'),
        ('orange_money', 'Orange Money'),
        ('free_money', 'Free Money'),
        ('carte', 'Carte bancaire'),
    ]
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('recu', 'Reçu'),
        ('echec', 'Échec'),
    ]

    nom_donateur = models.CharField(max_length=200, blank=True, default='Anonyme')
    email = models.EmailField(blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    montant = models.DecimalField(max_digits=10, decimal_places=0)
    methode = models.CharField(max_length=20, choices=METHODE_CHOICES)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    reference = models.CharField(max_length=100, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom_donateur} — {self.montant} FCFA ({self.methode})"

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Don"
        verbose_name_plural = "Dons"