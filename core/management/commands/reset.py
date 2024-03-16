from django.core.management import call_command
from django.core.management.base import BaseCommand
from core import models
import os

class Command(BaseCommand):
    def handle(self, *args, **options):
        os.system('pyclean .')

        try:
            for root, _, files in os.walk('core/migrations'):
                for file in files:
                    if file != '__init__.py':
                        os.remove(os.path.join(root, file))
        except:
            pass
        
        call_command('clean')
        call_command('makemigrations')
        call_command('migrate')
        call_command('fake')

        os.system('pyclean .')