# #!/usr/bin/env python
# """Django's command-line utility for administrative tasks."""
# import os
# import sys

# # from django.core.management import execute_from_command_line
# from django.core.management.commands.runserver import Command as runserver


# def main():
#     """Run administrative tasks."""
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cn334.settings')

#     try:
#         from django.core.management import execute_from_command_line
#     except ImportError as exc:
#         raise ImportError(
#             "Couldn't import Django. Are you sure it's installed and "
#             "available on your PYTHONPATH environment variable? Did you "
#             "forget to activate a virtual environment?"
#         ) from exc
#     execute_from_command_line(sys.argv)


# if __name__ == '__main__':
#     main()


# ^^^^^ Old code ^^^^^


# New code for using RunServerCommand to reload website on code automatically

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.management.commands.runserver import Command as RunserverCommand
from django.core.management import execute_from_command_line


class Command(RunserverCommand):
    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument('--noreload', action='store_false', dest='use_reloader', default=True,
                            help='Tells Django to NOT use the auto-reloader.')

    def handle(self, *args, **options):
        # Set to False if you want to disable the reloader
        options['use_reloader'] = True
        super().handle(*args, **options)


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cn334.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
