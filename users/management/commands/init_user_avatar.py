from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):

    help = "This command initiates avatar of all Users"

    def handle(self, *args, **options):

        users = User.objects.all()
        for user in users:
            user.avatar.delete()

        self.stdout.write(self.style.SUCCESS("init avatar work done."))
