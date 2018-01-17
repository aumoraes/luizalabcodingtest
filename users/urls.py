from django.urls import re_path
from users.views import RegisterUserView
from django.contrib.auth.views import login, logout_then_login


urlpatterns = [
    re_path(r'^registeradmin/$', RegisterUserView.as_view(), name="registeradmin"),
    re_path(r'^login/$', login, { 'template_name' : 'login.html', 'redirect_authenticated_user': '/'}, name="login" ),
    re_path(r'^logout/$', logout_then_login, { 'login_url' : '/'}, name="logout"),
]
