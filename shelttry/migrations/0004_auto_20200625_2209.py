# Generated by Django 2.1.3 on 2020-06-25 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelttry', '0003_auto_20200625_2149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='image',
        ),
        migrations.AddField(
            model_name='upload',
            name='image1',
            field=models.FileField(null=True, upload_to='pics/'),
        ),
        migrations.AddField(
            model_name='upload',
            name='image2',
            field=models.FileField(null=True, upload_to='pics/'),
        ),
        migrations.AddField(
            model_name='upload',
            name='image3',
            field=models.FileField(null=True, upload_to='pics/'),
        ),
        migrations.AddField(
            model_name='upload',
            name='image4',
            field=models.FileField(null=True, upload_to='pics/'),
        ),
    ]
