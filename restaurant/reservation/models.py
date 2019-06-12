from django.db import models
from phone_field import PhoneField
# Create your models here.

class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = PhoneField(blank=True, help_text='Contact phone number')
    number_of_persons = models.IntegerField()
    Date = models.DateField()
    time = models.TimeField()
    objects = models.Manager()


    def __str__(self):
        return self.name