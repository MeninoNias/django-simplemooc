from django import forms


class ContatoCurso(forms.Form):

    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    menssagem = forms.CharField(label='Menssagem/Duvida', widget=forms.Textarea)
    