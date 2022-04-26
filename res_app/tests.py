from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.core.exceptions import ValidationError
import datetime
from res_app.models import Reservation,Rental
import unittest

class ReservationListViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("reservation-list")
        
        self.rental_1 = Rental.objects.create(name="Ahmed")
    
        number_of_reservation = 11

        for reservation_id in range(1,number_of_reservation+1):
            checkin_day = reservation_id
            checkout_day = reservation_id + 1
            Reservation.objects.create(
                rental=self.rental_1,
                checkin=datetime.date(2022, 2, checkin_day),
                checkout=datetime.date(2022, 2, checkout_day),
            )
        
        
    def test_reservation_view_url_exists_at_desired_location(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
    def test_reservation_view_url_accessible_by_name(self):
        response = self.client.get(reverse('reservation-list'))
        self.assertEqual(response.status_code, 200)
    
    def test_previous_id_reservation(self):
        response = self.client.get(reverse('reservation-list'))
        self.assertEqual(response.status_code, 200)
        previous = ''
        for reservation in response.context['reservation_list']:
            if previous == '':
                previous = reservation.id
            else:
                self.assertEqual(previous , reservation.previous_reservation)
                previous = reservation.id


    


    
    

