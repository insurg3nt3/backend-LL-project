from django.db import models

# Create your models here.

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    inventory = models.PositiveSmallIntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveSmallIntegerField()
    booking_date = models.DateField()

    def get_item(self):
        return f'{self.name} : {str(self.no_of_guests)} : {str(self.booking_date)}'