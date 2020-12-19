#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import csv


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'booksapi.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

    from books import models
    path = "/Users/luke/PycharmProjects/Projects/micropythonapi/bestsellers-with-categories.csv"
    with open(path) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            _, created = models.Book.objects.get_or_create(
                name = row[0],
                author = row[1],
                rating = row[2],
                reviews = row[3],
                price = row[4],
                year = row[5],
                genre = row[6],
            )

if __name__ == '__main__':
    main()
