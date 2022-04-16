from django.db import models
from django.core.exceptions import ValidationError
class Rental(models.Model):
    name = models.CharField(max_length=100) 

class Reservation(models.Model):
    rental_id = models.ForeignKey(Rental,on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()

    class Meta:
        ordering = ['id','checkin','checkout']

    def clean(self):
        if self.checkout < self.checkin:
            raise ValidationError("checkout date should be greater than checkin date.")

    def previous_reservation(self):
        try:
            return Reservation.objects.filter(
                        checkin__lt=self.checkin,
                        rental_id=self.rental_id
                    ).last()
        except:
            raise ValidationError('Error Previous Reservation')

