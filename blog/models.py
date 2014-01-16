from django.db import models

class Artigo(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    publicacao = models.DateTimeField()
	
class Book(models.Model):
    name = models.CharField(max_length=50)
    pub_date = models.DateField()