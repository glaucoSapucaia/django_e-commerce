from django.contrib.auth.models import User
from django import forms
from perfil import models

class PerfilForm(forms.ModelForm):
    class Meta:
        model = models.Perfil
        fields = '__all__'
        exclude = ('usuario',)

class UserForm(forms.ModelForm):
    password1 = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label='Confirmação da senha',
    )
    password2 = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label='Senha',
    )

    def __init__(self, usuario=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.usuario = usuario

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def clean(self):
        data = self.data
        cleaned = self.cleaned_data
        validation_error_msgs = {}

        user_data = cleaned.get('username')
        email_data = cleaned.get('email')
        password_data = cleaned.get('password')
        password2_data = cleaned.get('password2')

        user_db = User.objects.filter(username=user_data).first()
        email_db = User.objects.filter(email=email_data).first()

        error_msg_user_exists = 'Usuário já cadastrado'
        error_msg_email_exists = 'Email já cadastrado'
        error_msg_password_match = 'As senhas precisam ser iguais'
        error_msg_password_short = 'A senha precisa ter pelo menos seis caracteres'

        if self.usuario:
            if user_data != user_db.username:
                if user_db:
                    validation_error_msgs['username'] = error_msg_user_exists

            if email_data != email_db.email:
                if email_db:
                    validation_error_msgs['email'] = error_msg_email_exists

            if password_data:
                if password_data != password2_data:
                    validation_error_msgs['password1'] = error_msg_password_match
                    validation_error_msgs['password2'] = error_msg_password_match

                if len(password_data) < 6:
                    validation_error_msgs['password1'] = error_msg_password_short
        else:
            pass

        if validation_error_msgs:
            raise forms.ValidationError(
                validation_error_msgs
            )