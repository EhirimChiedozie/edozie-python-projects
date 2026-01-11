from django.shortcuts import render
from .forms import EncryptionForm, DecryptionForm
from .utils import vigenere_encrypt, vigenere_decrypt
from django.http import HttpResponse


# Create your views here.

def cryptology_home(request):
    return render(request, 'cryptology/cryptology_home.html')


def vigenere_home(request):
    return render(request, 'cryptology/vigenere_home.html')

def vigenere_encryption(request):
    if request.method == 'POST':
        form = EncryptionForm(request.POST)
        if form.is_valid():
            plaintext = form.cleaned_data.get('plaintext')
            key = form.cleaned_data.get('key')
            ciphertext = vigenere_encrypt(plaintext, key)
            return HttpResponse(f'{ciphertext}')
    else:
        form = EncryptionForm()
    context = {'form': form}
    return render(request, 'cryptology/vigenere_encrypt.html', context=context)


def vigenere_decryption(request):
    if request.method == 'POST':
        form = DecryptionForm(request.POST)
        if form.is_valid():
            ciphertext = form.cleaned_data.get('ciphertext')
            key = form.cleaned_data.get('key')
            plaintext = vigenere_decrypt(ciphertext, key)
            return HttpResponse(f'{plaintext}')
    else:
        form = DecryptionForm()
    context = {'form': form}
    return render(request, 'cryptology/vigenere_decrypt.html', context=context)