from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import get_object_or_404, render

from .models import Author, Quote, Tag


def quote_list(request):
    quotes = Quote.objects.select_related("author").prefetch_related("tags")

    paginator = Paginator(quotes, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    top_tags = Tag.objects.annotate(
        quote_count=Count("quotes")
    ).order_by("-quote_count")[:10]

    return render(
        request,
        "quotes/quote_list.html",
        {
            "page_obj": page_obj,
            "top_tags": top_tags,
        },
    )

def tag_quotes(request, tag_name):
    quotes = (
        Quote.objects
        .filter(tags__name=tag_name)
        .select_related("author")
        .prefetch_related("tags")
    )

    paginator = Paginator(quotes, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "quotes/quote_list.html",
        {
            "page_obj": page_obj,
            "tag_name": tag_name,
        },
    )


def author_detail(request, fullname):
    author = get_object_or_404(Author, fullname=fullname)

    quotes = author.quotes.all()

    return render(
        request,
        "quotes/author_detail.html",
        {
            "author": author,
            "quotes": quotes,
        },
    )
