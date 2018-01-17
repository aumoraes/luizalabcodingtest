from django.views.generic.base import View
from django.shortcuts import render
from django.http import HttpResponseForbidden, HttpResponse
from employee.api import EmployeeApi
from django.conf import settings
from django.contrib.auth.decorators import  login_required
from rest_framework.decorators import detail_route

from django.contrib.auth.models import User

def index(request):
    has_logged_user = False
    logged_profile = None

    try:
        if request.user.is_authenticated:
            has_logged_user = True
            logged_profile = request.user

    except Exception as error:
        print("Error occur: %s" %(error))

    employees_list = EmployeeApi.list(None, request.GET.get('page', '1'))
    return render(request, "index.html", {'logged_profile': request.user, 'has_logged_user':has_logged_user, 'employees_list': employees_list, 'page_size': settings.REST_FRAMEWORK['PAGE_SIZE']})
