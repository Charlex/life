import os
from datetime import datetime
from django.conf import settings
from newsletters.models import NewsletterEmbed
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Sync embeds to p2p'

    def handle(self, *args, **options):
        for obj in NewsletterEmbed.objects.all():
            obj.publish_to_p2p()
