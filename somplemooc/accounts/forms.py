from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(forms.ModelForm):
    
    password1 = forms.CharField(label='senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmação de senha', widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Confirmação de senha não esta correta')
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])  
        if commit:
            user.save()
        
        return user

    class Meta:
        model = User
        fields = ['username', 'email']


class EditarAccountForm(forms.ModelForm):

    class Meta:
        
        model = User
        fields = ['username', 'email', 'name']


class PasswordResetForm(forms.Form):

    email = forms.EmailField(label='E-mail')

    def clean_email(self):
        email = self.cleaned_data['email']
        if(User.objects.filter(email=email).exists()):
            return email
        raise forms.ValidationError('Nenhum usuario encontrado com este e-mail')    
    