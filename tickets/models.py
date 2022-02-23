from django.db import models

# Create your models here.
from flights.models import Flight


class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.PROTECT)
    num_people = models.IntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)


class Ticket(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.PROTECT)
    seat = models.CharField(max_length=10)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    ticket_class = models.CharField(
        max_length=1,
        choices=[
            ('F', 'First Class'),
            ('B', 'Business Class'),
            ('M', 'Main Cabin'),
        ]
    )
