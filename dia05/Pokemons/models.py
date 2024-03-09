from django.db import models

# Create your models here.
class Pokemon(models.Model):
    nomePokemon = models.CharField(verbose_name="Nome do Pokemon", max_length=20)
    habilidade = models.CharField(verbose_name="Habilidades",max_length=30,blank=True,null=True)
    altura = models.IntegerField(verbose_name="Altura",blank=True,null=True)
    pokedexId = models.IntegerField(verbose_name="Id na Pokedex",blank=True,null=True)
    peso = models.IntegerField(verbose_name="Peso",blank=True,null=True)
    tipagem = models.CharField(verbose_name="Tipagem",max_length=30,blank=True,null=True)

    def __str__(self) -> str:
        return f"{self.nomePokemon} Pokedex number {self.pokedexId}"    