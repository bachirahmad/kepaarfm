from django.db import models # type: ignore

class Programme(models.Model):
    JOUR_CHOICES = [
        ('lundi', 'Lundi'), ('mardi', 'Mardi'),
        ('mercredi', 'Mercredi'), ('jeudi', 'Jeudi'),
        ('vendredi', 'Vendredi'), ('samedi', 'Samedi'),
        ('dimanche', 'Dimanche'),
    ]
    LANGUE_CHOICES = [
        ('wolof', 'Wolof'), ('francais', 'Français'),
        ('arabe', 'Arabe'), ('wolof_fr', 'Wolof / Français'),
    ]

    nom = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    animateur = models.ForeignKey('animateurs.Animateur', on_delete=models.SET_NULL, null=True, blank=True)
    jour = models.CharField(max_length=10, choices=JOUR_CHOICES)
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    langue = models.CharField(max_length=20, choices=LANGUE_CHOICES)
    icone = models.CharField(max_length=10, default='🎙️')
    actif = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nom} — {self.jour} {self.heure_debut}"

    class Meta:
        ordering = ['jour', 'heure_debut']
        verbose_name = "Programme"
        verbose_name_plural = "Programmes"