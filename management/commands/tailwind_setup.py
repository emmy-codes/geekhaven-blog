from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Install and build Tailwind CSS'

    def handle(self, *args, **kwargs):
        call_command('tailwind', 'install')
        call_command('tailwind', 'build')
