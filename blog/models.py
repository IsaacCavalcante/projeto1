from datetime import datetime
from django.db import models

class Artigo(models.Model):
    class Meta:
        ordering = ('-publicacao',)

    titulo = models.CharField(max_length=100)
    link = models.TextField()
    tema = models.TextField()
    tipo = models.TextField()
    publicacao = models.DateTimeField(default=datetime.now, blank=True)
    link_qrcode = models.TextField()

    def get_absolute_url(self):
        return '/artigo/%d/'%self.id

class Book(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=500)
    pub_date = models.DateField()