from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.conf import settings
from django.core.validators import RegexValidator
# Create your models here.
from django.shortcuts import reverse

type = [
    ['Flat', 'Flat'],
    ['Self contain', 'Self contain'],
    ['Single room', 'Single room'],
]

town = [
    ['Ago', 'Ago'],
    ['Igbo_Igbo', 'Ijebu Igbo'],
    ['Oru', 'Oru'],
]


default = 'pics'

class Houses(models.Model):
    hallname = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    type = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    price = models.PositiveIntegerField("Price")
    landlord_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to=default, default=default)
    image2 = models.ImageField(upload_to=default, default=default)
    image3 = models.ImageField(upload_to=default, default=default)
    image4 = models.ImageField(upload_to="pics/%s-%s", default="pics/%s-%s")


class Test(models.Model):
    hallname = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    type = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    price = models.PositiveIntegerField("Price")
    landlord_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=100)


class TestImages(models.Model):
    test = models.ForeignKey(Test, default=1, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pics',
                              verbose_name='Image')




class Signup(models.Model):
    firstname = models.CharField(max_length=100)
    email = models.CharField(max_length=500)
    password = models.CharField(max_length=100)
    password1 = models.CharField(max_length=100)


class Subscribe(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)




class Post(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    hallname = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    type = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    price = models.PositiveIntegerField("Price")
    landlord = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.PositiveIntegerField()

'''
def get_image_filename(instance, filename):
    id = instance.post.id
    return "post_images/%s" % (id)
'''

class Images(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pics',
                              verbose_name='Image')


class Upload(models.Model):
    hallname = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    type = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    availability = models.CharField(max_length=100)
    price = models.PositiveIntegerField("Price")
    landlord = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    extra_facility = models.CharField(max_length=1000)
    numbers = models.IntegerField(null=True)
    image1 = models.FileField(upload_to='pics/', null=True)
    image2 = models.FileField(upload_to='pics/', null=True)
    image3 = models.FileField(upload_to='pics/', null=True)
    image4 = models.FileField(upload_to='pics/', null=True)
    image5 = models.FileField(upload_to='pics/', null=True)
    image6 = models.FileField(upload_to='pics/', null=True)
    image7 = models.FileField(upload_to='pics/', null=True)
    image8 = models.FileField(upload_to='pics/', null=True)
    image9 = models.FileField(upload_to='pics/', null=True)
    image10 = models.FileField(upload_to='pics/', null=True)


    def __str__(self):
        return str(self.hallname)

