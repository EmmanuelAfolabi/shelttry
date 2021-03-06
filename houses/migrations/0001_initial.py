# Generated by Django 2.2.6 on 2020-01-19 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hallname', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('landlord_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone_number', models.TextField()),
                ('document1', models.ImageField(upload_to='pics')),
                ('document2', models.ImageField(upload_to='pics')),
                ('document3', models.ImageField(upload_to='pics')),
                ('document4', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
    ]
