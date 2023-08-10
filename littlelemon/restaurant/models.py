from django.db import models

# Create your models here.

class Menu(models.Model):
    ID = models.AutoField(max_length=5, primary_key=True)
    Title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    Inventory = models.IntegerField(max_length=5)

    def __str__(self):
        return self.Title

class Booking(models.Model):
    ID = models.AutoField(max_length=10, primary_key=True)
    name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(max_length=5)
    Booking_date = models.DateField()

    def __str__(self):
        return self.name