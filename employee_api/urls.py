from django.urls import include, re_path
from employee_api.api_views.employee import EmployeeViewSet
from employee_api.router import EmployeeRouter

employee_router = EmployeeRouter()
employee_router.register(r'employee', EmployeeViewSet, base_name="Employee")



urlpatterns = [
    re_path(r'^', include(employee_router.urls)),
]
