from django.db import models

# Create your models here.
class RegistroJuridico(models.Model):
    FAVOR = (
        ('0','Contrário ao Cliente'),
        ('1','Parcialmente Favorável'),
        ('2','Favorável ao Cliente'),
    )

    n_processo =  models.CharField(max_length=30)
    id_cliente =  models.IntegerField(db_index=True)
    favor_contribuinte =  models.CharField(max_length=2, db_index=True,choices=FAVOR)
    ementa = models.TextField()
    

