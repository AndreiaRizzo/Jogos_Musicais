from django.db import models

# Create your models here.
# nome_da_aplicacao/models.py


class Jogo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    nivel_dificuldade = models.CharField(max_length=50)
    url_jogo = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    avatar = models.CharField(max_length=100, default="avatar1")  # Novo campo para armazenar o avatar
    
    def __str__(self):
        return self.nome

class Pontuacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    pontuacao = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.usuario} - {self.jogo} - {self.pontuacao}"

