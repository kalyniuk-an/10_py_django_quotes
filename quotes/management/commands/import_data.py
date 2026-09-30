import json

from django.core.management.base import BaseCommand

from quotes.models import Author, Quote, Tag


class Command(BaseCommand):
    help = "Import authors and quotes from JSON files"

    def handle(self, *args, **options):
        with open("authors.json", "r", encoding="utf-8") as file:
            authors = json.load(file)

        for author_data in authors:
            Author.objects.get_or_create(
                fullname=author_data["fullname"],
                defaults={
                    "born_date": author_data["born_date"],
                    "born_location": author_data["born_location"],
                    "description": author_data["description"],
                },
            )

        self.stdout.write(
            self.style.SUCCESS(f"Imported {len(authors)} authors")
        )

# Import quotes
        with open("quotes.json", "r", encoding="utf-8") as file:
            quotes = json.load(file)

        for quote_data in quotes:
            author = Author.objects.get(fullname=quote_data["author"])

            quote, created = Quote.objects.get_or_create(
                text=quote_data["quote"],
                author=author,
            )

            for tag_name in quote_data["tags"]:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                quote.tags.add(tag)

        self.stdout.write(
            self.style.SUCCESS(f"Imported {len(quotes)} quotes")
        )
