from django.db import models
from django.conf import settings


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveIntegerField()


class HotelYourChoiceBooking(models.Model):
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveIntegerField()
    hotel = models.ForeignKey('HotelYourChoiceHotel',
                              on_delete=models.DO_NOTHING)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hotel_your_choice_booking'


class HotelYourChoiceHotel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'hotel_your_choice_hotel'
