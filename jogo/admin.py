# nome_da_aplicacao/admin.py

from django.contrib import admin
from .models import Jogo, Usuario, Pontuacao

@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nivel_dificuldade', 'url_jogo')  # Exibe esses campos na lista de jogos
    search_fields = ('nome', 'nivel_dificuldade')  # Permite busca por nome e nível de dificuldade
    list_filter = ('nivel_dificuldade',)  # Adiciona filtro para nível de dificuldade

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'avatar')  # Exibe nome e idade do usuário
    search_fields = ('nome',)  # Permite busca pelo nome do usuário

@admin.register(Pontuacao)
class PontuacaoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'jogo', 'pontuacao', 'data')  # Exibe usuário, jogo, pontuação e data
    list_filter = ('data',)  # Adiciona filtro para data
    search_fields = ('usuario__nome', 'jogo__nome')  # Permite busca pelo nome do usuário e do jogo
