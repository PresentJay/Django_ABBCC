import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):

    help = "This command creates many rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many rooms do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()

        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()

        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "price": lambda x: random.randint(1, 300),
                "guests": lambda x: random.randint(1, 5),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )

        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.HouseRule.objects.all()

        for pk in created_clean:
            # get each key of created_room
            room = room_models.Room.objects.get(pk=pk)

            # add randomized photo
            for i in range(2, random.randint(4, 8)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"room_photos/{random.randint(1,51)}.jpg",
                )

            # the methods of below are about "many to many field"

            # add randomized amenities
            for a in amenities:
                if random.randint(0, 30) % 2 == 0:
                    room.amenities.add(a)

            # add randomized facilites
            for f in facilities:
                if random.randint(0, 2) % 2 == 0:
                    room.facilities.add(f)

            # add randomized house_rules
            for r in rules:
                if random.randint(0, 2) % 2 == 0:
                    room.house_rules.add(r)

        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))
