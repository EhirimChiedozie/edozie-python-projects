from django.urls import path
from . import views

urlpatterns = [
    path('', views.enter_words, name='enter-words'),
    path('word_solution/', views.word_solution, name='word-solution'),
]