from django.urls import path
from . import views

urlpatterns = [
    path('', views.cryptology_home, name='cryptology-home'),
    path('vigenere-home/', views.vigenere_home, name='vigenere-home'),
    path('vigenere-encryption/', views.vigenere_encryption, name='vigenere-encryption'),
    path('vigenere-decryption/', views.vigenere_decryption, name='vigenere-decryption'),
]