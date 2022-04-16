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
print('**'*10 + 'It will take between 10 to 30 second to create the data' + '**'*10)
rental_1 = Rental.objects.create(name='rental-1')

number_of_data = 1100

INITAL_DATE = datetime.date(2022, 1, 13)

for increament in range(2,number_of_data+2):

    Reservation.objects.create(
        rental_id=rental_1,
        checkin=INITAL_DATE + datetime.timedelta(days=increament-1),
        checkout=INITAL_DATE + datetime.timedelta(days=increament),
    )

#####


