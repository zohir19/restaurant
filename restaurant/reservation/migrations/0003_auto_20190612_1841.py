# Generated by Django 2.1.5 on 2019-06-12 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_auto_20190612_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='phone',
            field=models.IntegerField(),
        ),
    ]