from django.core.management.base import BaseCommand
from story.utils.fetch_json_info import fetch_and_store_json_info

class Command(BaseCommand):
    help = 'Execute custom command.'
    def handle(self, *args, **kwargs):
        fetch_and_store_json_info()
        self.stdout.write(self.style.SUCCESS('Task accomplished.'))
