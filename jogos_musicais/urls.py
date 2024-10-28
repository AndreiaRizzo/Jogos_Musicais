
from django.contrib import admin
from django.urls import include,path
from jogo import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz-instrumento/', views.quiz_instrumento, name='quiz_instrumento'),
    path('jogo/<int:jogo_id>/', views.jogo_detalhes, name='jogo_detalhes'),  # URL para detalhes do jogo
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('registrar-pontuacao/', views.registrar_pontuacao, name='registrar_pontuacao'),

]
