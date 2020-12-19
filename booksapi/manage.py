#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


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

    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Teacher.objects.get_or_create(
                first_name=row[0],
                last_name=row[1],
                middle_name=row[2],
            )

if __name__ == '__main__':
    main()
