# Generated by Django 2.2.6 on 2020-02-22 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='House',
        ),
        migrations.DeleteModel(
            name='Subscribe',
        ),
    ]
