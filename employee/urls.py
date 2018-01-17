from django.urls import include, path, re_path
from employee.view.index_view import index
from employee.view.manage_view import manage
from employee.view.register_view import RegisterView


urlpatterns = [
    re_path(r'^$', index, name="index"),
    re_path(r'^register/$', RegisterView.as_view(), name="register"),
    re_path(r'^employee/(?P<employee_id>\d+)$', manage, name="manage"),
    re_path(r'^employee/', index, name="index_list"),
]
