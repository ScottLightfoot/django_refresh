'''
Django cmd to wait for db availability
'''
import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    '''dj cmd to wait for db'''

    def handle(self, *args, **options):
        '''Entrypoint for cmd'''
        self.stdout.write('Waiting for db...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('db unavailable, waiting 1 sec...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('DB Available!'))
