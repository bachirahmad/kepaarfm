from django.db import models # type: ignore

class Animateur(models.Model):
    nom = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    emission_principale = models.CharField(max_length=200, blank=True)
    biographie = models.TextField(blank=True)
    photo = models.ImageField(upload_to='animateurs/', blank=True, null=True)
    actif = models.BooleanField(default=True)
    ordre = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nom

    class Meta:
        ordering = ['ordre', 'nom']
        verbose_name = "Animateur"
        verbose_name_plural = "Animateurs"