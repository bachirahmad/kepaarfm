from django.db import models # type: ignore 

class TypeEmission(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    icone = models.CharField(max_length=10, default='🎙️')
    couleur = models.CharField(max_length=20, default='green')

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Type d'émission"
        verbose_name_plural = "Types d'émissions"


class Emission(models.Model):
    LANGUE_CHOICES = [
        ('wolof', 'Wolof'),
        ('francais', 'Français'),
        ('arabe', 'Arabe'),
        ('wolof_fr', 'Wolof / Français'),
    ]

    titre = models.CharField(max_length=200)
    type_emission = models.ForeignKey(TypeEmission, on_delete=models.SET_NULL, null=True)
    animateur = models.ForeignKey('animateurs.Animateur', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)
    fichier_audio = models.FileField(upload_to='emissions/audio/')
    image = models.ImageField(upload_to='emissions/images/', blank=True, null=True)
    langue = models.CharField(max_length=20, choices=LANGUE_CHOICES, default='wolof')
    date_diffusion = models.DateField()
    duree = models.CharField(max_length=20, blank=True)  # Ex: "45:22"
    nb_ecoutes = models.PositiveIntegerField(default=0)
    publie = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

    class Meta:
        ordering = ['-date_diffusion']
        verbose_name = "Émission"
        verbose_name_plural = "Émissions"