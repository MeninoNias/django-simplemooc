from django import forms
from django.core.mail import send_mail
from django.conf import settings 

from somplemooc.core.mail import send_mail_template

class ContatoCurso(forms.Form):

    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    menssagem = forms.CharField(label='Menssagem/Duvida', widget=forms.Textarea)
    

    def send_mail(self):
        subject = 'CONTATO: Curso SimpleMooc'
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['menssagem'],
        }

        template_name = 'courses/contato_mail.html'
        send_mail_template(subject, template_name, context, [settings.CONTACT_EMAIL])
       
       
       
        # subject = 'Contato'
        # menssagem = 'Nome: %(name)s; E-mail: %(email)s; %(menssagem)s'
        # context = {
        #     'name': self.cleaned_data['name'],
        #     'email': self.cleaned_data['email'],
        #     'menssagem': self.cleaned_data['menssagem'],
        # } 

        # menssagem = menssagem % context

        # send_mail(subject, menssagem, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])
        