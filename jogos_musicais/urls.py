
from django.contrib import admin
from django.urls import include,path
from jogo import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz-instrumento/', views.quiz_instrumento, name='quiz_instrumento'),
     path('', views.home, name='home'),

]
