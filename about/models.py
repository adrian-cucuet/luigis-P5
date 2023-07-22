from django.db import models
from datetime import datetime

TIME = (
    ('12.00 - 13.00', '12.00 - 13.00'),
    ('13.00 - 14.00', '13.00 - 14.00'),
    ('14.00 - 15.00', '14.00 - 15.00'),
    ('15.00 - 16.00', '15.00 - 16.00'),
    ('16.00 - 17.00', '16.00 - 17.00'),
    ('17.00 - 18.00', '17.00 - 18.00'),
    ('18.00 - 19.00', '18.00 - 19.00'),
    ('19.00 - 20.00', '19.00 - 20.00'),
    ('20.00 - 21.00', '20.00 - 21.00'),
    )


class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=False, blank=False)
    no_of_guests = models.IntegerField()
    date = models.DateField()
    time = models.CharField(max_length=15, choices=TIME, default=TIME[0])

    def __str__(self):
        return self.name