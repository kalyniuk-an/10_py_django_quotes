from django.contrib.auth.views import (
LoginView,
LogoutView,
PasswordResetView,
PasswordResetDoneView,
PasswordResetConfirmView,
PasswordResetCompleteView,
)
from django.urls import path

from .views import (
    add_author,
    add_quote,
    author_detail,
    quote_list,
    register,
    tag_quotes,
)

urlpatterns = [
    path("", quote_list, name="quote_list"),
    path("tag/<str:tag_name>/", tag_quotes, name="tag_quotes"),
    path("author/add/", add_author, name="add_author"),
    path("author/<str:fullname>/", author_detail, name="author_detail"),
    path("quote/add/", add_quote, name="add_quote"),
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
    path(
        "password-reset/",
        PasswordResetView.as_view(
            template_name="registration/password_reset_form.html",
            email_template_name="registration/password_reset_email.html",
            subject_template_name="registration/password_reset_subject.txt",
            success_url="/password-reset/done/",
        ),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        PasswordResetDoneView.as_view(
            template_name="registration/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password-reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="registration/password_reset_confirm.html",
            success_url="/password-reset/complete/",
        ),
        name="password_reset_confirm",
        ),
    path(
        "password-reset/complete/",
        PasswordResetCompleteView.as_view(
            template_name="registration/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),

]