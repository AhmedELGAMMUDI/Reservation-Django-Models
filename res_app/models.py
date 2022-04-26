from django.db import models
from django.core.exceptions import ValidationError

class Rental(models.Model):
    name = models.CharField(max_length=100) 

class Reservation(models.Model):
    rental = models.ForeignKey(Rental,on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()

    class Meta:
        ordering = ['checkin','checkout']

    def clean(self):
        if self.checkout < self.checkin:
            raise ValidationError("checkout date should be greater than checkin date.")


