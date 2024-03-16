from django.core.management.base import BaseCommand
from core import models
import random

class Command(BaseCommand):
    def handle(self, *args, **options):
        for seactr in range(1, 2):
            season = models.Season()
            season.name = f'Season {seactr}'
            season.save()
            prevdis, prevpri = 0, 0
            for quectr in range(1, 51):
                prevdis += random.randint(1, 10)
                prevpri += random.randint(1, 10)

                quest = models.Quest()
                quest.name = f'Quest {quectr}'
                quest.description = f'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec diam lorem.'
                quest.distance = prevdis
                quest.prize = prevpri
                quest.season = season
                quest.save()