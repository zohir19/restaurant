# Generated by Django 2.1.5 on 2019-06-12 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': ' category', 'verbose_name_plural': 'catogories'},
        ),
    ]
