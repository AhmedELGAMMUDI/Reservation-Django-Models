# Generated by Django 3.2.4 on 2022-04-25 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('res_app', '0003_rename_rental_reservation_rental_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='rental_id',
            new_name='Rental',
        ),
    ]