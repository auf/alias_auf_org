from django.db import models

# Create your models here.

USAGE = (
    ("INTERNE", "à l'usage interne de l'AUF"),
    ("PUBLIC", "à usage public"),
    ("TECH", "à usage technique"),
)

ETAT = (
    ("OK", "alias fonctionnel"),
    ("SUPPRIME", "alias supprimé"),
    ("A SUPPRIMER", "alias à supprimer"),
    ("A VERIFIER", "alias à vérifier"),
)

PUBLICATION = (
    ("PUB", "publié"),
    ("PRV", "non publié"),
)

class Alias(models.Model):
    nom = models.CharField(
        "nom de l'alias", max_length=240, primary_key=True
    )
    date_creation = models.DateTimeField(
        "date de création", auto_now_add=True
    )
    usage = models.CharField(
        "à usage interne ou public", max_length=16,
        choices=USAGE, default=USAGE[0][0], blank=False
    )
    responsable = models.CharField(
        "nom du responsable de l'alias", max_length=256
    )
    etat = models.CharField(
        "quel est l'état de l'alias", max_length=64, choices=ETAT,
        default=ETAT[0][0], blank=False
    )
    observations = models.TextField("Observations", max_length=256, blank=True)
    publication = models.CharField(
        "publication sur le web", max_length=4, choices=PUBLICATION,
        default=PUBLICATION[0][0], blank=False
    )
    
    class Meta:
        verbose_name = verbose_name_plural = 'alias'
        ordering = ['nom']

    def __unicode__(self):
        return self.nom