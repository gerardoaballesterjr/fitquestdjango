from django.core.management.base import BaseCommand
from dotenv import dotenv_values
import psycopg2

class Command(BaseCommand):
    def handle(self, *args, **options):
        env = dotenv_values('.env')
        
        connection = psycopg2.connect(
            dbname=str(env['DB_NAME']),
            user=str(env['DB_USER']),
            password=str(env['DB_PASSWORD']),
            host=str(env['DB_HOST']),
            port=int(env['DB_PORT']),
        )

        cursor = connection.cursor()

        cursor.execute("drop schema public cascade; create schema public;")

        connection.commit()

        cursor.close()
        connection.close()