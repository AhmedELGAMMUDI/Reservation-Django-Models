import django, os, sys
import datetime
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "reservation.settings")
sys.path.append(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", ".."))
django.setup()

from res_app.models import Reservation,Rental
from django.core import management

# Migrate
management.call_command("migrate", no_input=True)
management.call_command("makemigrations", no_input=True)

# Seed
rental_1 = Rental.objects.create(name='rental-1')
rental_2 = Rental.objects.create(name='rental-2')

Reservation.objects.create(
    rental_id=rental_1,
    checkin=datetime.date(2022, 1, 1),
    checkout=datetime.date(2022, 1, 13),
)
Reservation.objects.create(
    rental_id=rental_1,
    checkin=datetime.date(2022, 1, 20),
    checkout=datetime.date(2022, 2, 10),
)
Reservation.objects.create(
    rental_id=rental_1,
    checkin=datetime.date(2022, 2, 20),
    checkout=datetime.date(2022, 3, 10),
)

Reservation.objects.create(
    rental_id=rental_2,
    checkin=datetime.date(2022, 1, 2),
    checkout=datetime.date(2022, 1, 20),
)
Reservation.objects.create(
    rental_id=rental_2,
    checkin=datetime.date(2022, 1, 20),
    checkout=datetime.date(2022, 2, 11),
)


#####


