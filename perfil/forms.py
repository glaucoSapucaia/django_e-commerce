from typing import Any
from django.contrib.auth.models import User
from django import forms
from perfil import models

class PerfilForm(forms.ModelForm):
    class Meta:
        model = models.Perfil
        fields = '__all__'
        exclude = ('usuario',)

class UserForm(forms.ModelForm):
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label='Senha',
    )

    def __init__(self, usuario=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.usuario = usuario

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

    def clean(self) -> dict[str, Any]:
        data = self.data
        cleaned = self.cleaned_data
        return super().clean()