from django.db import models

# Create your models here.
class Nuit_applicatif(models.Model):
    type_na                = models.CharField(max_length=120, null=True)
    Environnement_na       = models.CharField(max_length=120, null=True)
    Date_na                = models.DateField()
    Durée_na               = models.DecimalField(decimal_places=2, max_digits=1000000)
    moyenne_execution_na   = models.DecimalField(decimal_places=2, max_digits=1000000)


class Detail_na(models.Model):
    nuit_applicatif        = models.ForeignKey(Nuit_applicatif, on_delete=models.CASCADE, null=True)
    Nom_job                = models.CharField(max_length=120, null=True)
    Date_heure_debut_na    = models.DateTimeField()
    Date_heure_fin_na      = models.DateTimeField()
    Statut_job             = models.CharField(max_length=120, null=True)


class Detail_job(models.Model):
    detail_job             = models.ForeignKey(Detail_na, on_delete=models.CASCADE, null=True)
    moyenne_execution_job  = models.DecimalField(decimal_places=2, max_digits=1000000)