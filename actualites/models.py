from django.db import models # type: ignore

class Actualite(models.Model):
    CATEGORIE_CHOICES = [
        ('islam', 'Islam'),
        ('savoir', 'Savoir'),
        ('communaute', 'Communauté'),
        ('senegal', 'Sénégal'),
        ('monde', 'Monde'),
    ]

    titre = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, blank=True)
    categorie = models.CharField(max_length=20, choices=CATEGORIE_CHOICES)
    contenu = models.TextField()
    image = models.ImageField(upload_to='actualites/', blank=True, null=True)
    publie = models.BooleanField(default=True)
    en_une = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify # type: ignore
            self.slug = slugify(self.titre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titre

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Actualité"
        verbose_name_plural = "Actualités"  