from django import forms


class EncryptionForm(forms.Form):
    plaintext = forms.CharField(max_length=500)
    key = forms.CharField(max_length=500)



class DecryptionForm(forms.Form):
    ciphertext = forms.CharField(max_length=5000)
    key = forms.CharField(max_length=500)