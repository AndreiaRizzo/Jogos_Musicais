# nome_da_aplicacao/views.py

from django.shortcuts import render
import random


def home(request):
    return render(request, 'jogo/home.html')

def quiz_instrumento(request):
    # Dados do instrumento
    instrumento_correto = {
        "nome": "Trompete",
        "imagem_url": "jogo/static/jogo/imagens/trompeteCrian.jpg" # URL da imagem do instrumento
    }
    # Opções de resposta
    opcoes = ["Trompete", "Violino", "Piano"]
    random.shuffle(opcoes)  # Embaralha as opções para exibir em ordem aleatória

    # Verifica se há uma resposta no request
    resposta = request.GET.get("resposta")
    mensagem = ""
    if resposta:
        if resposta == instrumento_correto["nome"]:
            mensagem = "Parabéns! Você acertou."
        else:
            mensagem = "Resposta incorreta. Tente novamente!"

    return render(request, 'jogo/quiz_instrumento.html', {
        'instrumento': instrumento_correto,
        'opcoes': opcoes,
        'mensagem': mensagem
    })

