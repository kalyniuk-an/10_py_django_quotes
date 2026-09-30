from django.urls import path

from .views import author_detail, quote_list, tag_quotes


urlpatterns = [
    path("", quote_list, name="quote_list"),
    path("tag/<str:tag_name>/", tag_quotes, name="tag_quotes"),
    path("author/<str:fullname>/", author_detail, name="author_detail"),
]