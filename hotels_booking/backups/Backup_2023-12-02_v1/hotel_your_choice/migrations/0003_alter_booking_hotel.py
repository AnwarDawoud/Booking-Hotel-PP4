# Generated by Django 4.2.7 on 2023-12-01 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_your_choice', '0002_remove_booking_room_booking_hotel_alter_booking_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='hotel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel_your_choice.hotel'),
        ),
    ]