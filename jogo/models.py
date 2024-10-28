from django.db import models

# Create your models here.
# nome_da_aplicacao/models.py


class Jogo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    nivel_dificuldade = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
       
    def __str__(self):
        return self.nome

class Pontuacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    pontuacao = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.usuario} - {self.jogo} - {self.pontuacao}"

