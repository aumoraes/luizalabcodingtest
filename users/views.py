from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.base import View
from users.forms import RegistrarUsuarioForm

class RegisterUserView(View):
  template_name = "registeradmin.html"

  def get(self, request):
    return render(request, self.template_name)

  def post(self, request):
    form = RegistrarUsuarioForm(request.POST)
    if form.is_valid():
      dados_form = form.data
      user = User.objects.create_user(dados_form['nome'], dados_form['email'], dados_form['senha'])
      user.is_superuser = True
      user.is_staff = True
      user.save()

      return redirect('index')

    return render(request, self.template_name, { 'form': form })
