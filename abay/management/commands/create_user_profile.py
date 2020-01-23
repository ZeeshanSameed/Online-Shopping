from abay.models import *
from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    help = 'Create user profile'

    def handle(self, *args, **kwargs):
        users = User.objects.all()

        for user in users:
            ProfileModel.objects.create(user=user)