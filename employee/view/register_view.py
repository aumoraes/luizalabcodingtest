from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from employee.models.employee import Employee
from employee.forms import RegisterUserForm
from employee.api import EmployeeApi
from employee.builder_employee import BuildEmployeeJson

class RegisterView(View):
    template_name = "register.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):

        form = RegisterUserForm(request.POST)
        if form.is_valid():
            dados_form = form.data

            employee = BuildEmployeeJson.build( self, name = dados_form["name"], email = dados_form["email"], department = dados_form["department"] )

            EmployeeApi.create(self, employee)

            return redirect('index')

        return render(request, self.template_name, {'form': form})
