from django.db import models

# Create your models here.

from django.db import models

class Genero(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Continente(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Pais(models.Model):
    nome = models.CharField(max_length=50)
    continente = models.ForeignKey(Continente, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    site = models.URLField()
    insta = models.CharField(max_length=50)
    face = models.URLField()
    twitter = models.CharField(max_length=50)
    nacionalidade = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class Filme(models.Model):
    nome = models.CharField(max_length=100)
    duracao = models.IntegerField()  # Em minutos
    sinopse = models.TextField()
    site_oficial = models.URLField()
    data_lancamento = models.DateField()
    nota_avaliacao = models.DecimalField(max_digits=3, decimal_places=1)
    genero = models.ManyToManyField(Genero)
    pais = models.ManyToManyField(Pais)
    diretor = models.ManyToManyField(Pessoa, related_name='dirigiu_filmes')

    def __str__(self):
        return self.nome
    
class Ator(models.Model):
    nome = models.CharField(max_length=50)
    filmes = models.ManyToManyField(Filme, related_name='atores')

    def __str__(self):
        return self.nome
    
class Serie(models.Model):
    nome = models.CharField(max_length=100)
    duracao = models.IntegerField()  # Em minutos por episódio
    sinopse = models.TextField()
    site_oficial = models.URLField()
    data_lancamento = models.DateField()
    nota_avaliacao = models.DecimalField(max_digits=3, decimal_places=1)
    genero = models.ManyToManyField(Genero)
    pais = models.ManyToManyField(Pais)
    diretor = models.ManyToManyField(Pessoa, related_name='dirigiu_series')

    def __str__(self):
        return self.nome
    
class Temporada(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Episodio(models.Model):
    nome = models.CharField(max_length=100)
    duracao = models.IntegerField()  # Em minutos
    data_disponibilizacao = models.DateField()
    temporada = models.ForeignKey(Temporada, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome