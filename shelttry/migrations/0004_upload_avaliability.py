# Generated by Django 2.1.3 on 2020-10-07 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelttry', '0003_auto_20200925_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='avaliability',
            field=models.CharField(default='Aavailable', max_length=100),
            preserve_default=False,
        ),
    ]