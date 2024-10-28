
from django.shortcuts import render, redirect, get_object_or_404
from .models import Jogo, Usuario, Pontuacao
import random 

def home(request):
    jogos = Jogo.objects.all()  # Obtém todos os jogos
    return render(request, 'jogo/home.html', {'jogos': jogos})

def jogo_detalhes(request, jogo_id):
    jogo = get_object_or_404(Jogo, id=jogo_id)
    return render(request, 'jogo/jogo_detalhes.html', {'jogo': jogo})

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        avatar = request.POST.get('avatar')  # Recebe o avatar selecionado

        # Cria um novo usuário com os dados recebidos
        novo_usuario = Usuario(nome=nome, idade=idade, avatar=avatar)
        novo_usuario.save()  # Salva no banco de dados
        return redirect('home')
        # Redirecionar ou renderizar um template após o cadastro
    return render(request, 'jogo/cadastro.html')

def registrar_pontuacao(request):
    if request.method == 'POST':
        usuario_id = request.POST.get('usuario')
        jogo_id = request.POST.get('jogo')
        pontuacao = request.POST.get('pontuacao')
        usuario = Usuario.objects.get(id=usuario_id)
        jogo = Jogo.objects.get(id=jogo_id)
        Pontuacao.objects.create(usuario=usuario, jogo=jogo, pontuacao=pontuacao)
        # Redirecionar ou renderizar um template após a pontuação ser registrada
    return render(request, 'jogo/registrar_pontuacao.html')



#joguinhos
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

