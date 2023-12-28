
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from perfil import models, forms

class BasePerfil(View):
    template_name = 'perfil/criar.html'

    def setup(self, *args, **kwargs) -> None:
        super().setup(*args, **kwargs)

        if self.request.user.is_authenticated:
            self.context = {
                'userform': forms.UserForm(
                    data=self.request.POST or None,
                    usuario=self.request.user,
                    instance=self.request.user,
                ),
                'perfilform': forms.PerfilForm(data=self.request.POST or None),
            }
        else:
            self.context = {
                'userform': forms.UserForm(data=self.request.POST or None),
                'perfilform': forms.PerfilForm(data=self.request.POST or None),
            }

        self.renderizar = render(self.request, self.template_name, self.context)
    
    def get(self, *args, **kwargs):
        return self.renderizar

class Criar(BasePerfil):
    def post(self, *args, **kwargs):
        return self.renderizar
    
class Atualizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Atualizar')

class Login(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Login')

class Logout(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Logout')
