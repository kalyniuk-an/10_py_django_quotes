from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import author_detail, quote_list, register, tag_quotes


urlpatterns = [
    path("", quote_list, name="quote_list"),
    path("tag/<str:tag_name>/", tag_quotes, name="tag_quotes"),
    path("author/<str:fullname>/", author_detail, name="author_detail"),
    path("register/", register, name="register"),
    path(
        "login/",
        LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(),
        name="logout",
    ),
]