# Generated by Django 2.1.5 on 2019-06-12 19:17

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0004_auto_20190612_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]