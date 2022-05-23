"""
Django Command to wait for database to be available
"""

import time

from psycopg2 import OperationalError as psycopg2Error

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """ Django Command to wait for databse """
    def handle(self, *args, **options):
        """ Entry Point for Command """

        self.stdout.write(" Waiting for Database... ")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (psycopg2Error, OperationalError):
                self.stdout.write(
                    "Databse not available wait for one Second ")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('DATABASE Available'))
