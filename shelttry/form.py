from django import forms
from .models import Post, Images, Upload
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


type = [
    ['Flat', 'Flat'],
    ['Self contain', 'Self contain'],
    ['Single room', 'Single room'],
]

town = [
    ['ago-iwoye', 'Ago'],
    ['ijebu-igbo', 'Ijebu Igbo'],
    ['oru', 'Oru'],
]

purp = [
    ['Rent', 'Rent'],
    ['Sale', 'Sale'],
]

availability = [
    ['Available', 'Available'],
    ['Not Available', 'Not Available'],
]

IMAGES_CHOICES = {
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('7', '7'),
    ('5', '5'),
    ('6', '6'),
    ('4', '4'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
}

class PostForm(forms.ModelForm):
    hallname = forms.CharField(label='Hall name', max_length=100)
    description = forms.CharField(label='Description', max_length=500)
    type = forms.CharField(label='Type', widget=forms.Select(choices=type))
    town = forms.CharField(label='Town', widget=forms.Select(choices=town))
    availability = forms.CharField(label='Availability', widget=forms.Select(choices=availability))
    price = forms.IntegerField(label='Price')
    landlord = forms.CharField(label="Agent's name", max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    phone = forms.CharField(label='Phone number', max_length=100)

    class Meta:
        model = Post
        fields = ('hallname', 'description', 'type',
                  'town', 'price', 'landlord', 'email', 'phone', )


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')
    class Meta:
        model = Images
        fields = ('image',)


class SignUpForm(UserCreationForm):
    #name = forms.CharField(max_length=30, required=True, help_text='Required. name')
    email = forms.EmailField(max_length=300, required=False, help_text='Optional. email')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CreateUserForm(UserCreationForm):
    fullname = forms.CharField(label='Full Name', max_length=500)

    class Meta:
        model = User
        fields = ['fullname', 'username', 'email', 'password1', 'password2']




class DocumentForm(forms.ModelForm):
    town = forms.CharField(label='Town', widget=forms.Select(choices=town))
    type = forms.CharField(label='Type', widget=forms.Select(choices=type))
    availability = forms.CharField(label='Availability', widget=forms.Select(choices=availability))
    description = forms.TextInput()
    landlord = forms.CharField(label='Username', max_length=500)
    numbers = forms.IntegerField(label="Numbers of images to be uploaded", widget=forms.Select(choices=IMAGES_CHOICES))
    
    image1 = forms.ImageField(label="1")
    image2 = forms.ImageField(label="2")
    image3 = forms.ImageField(label="3")
    image4 = forms.ImageField(label="4")
    image5 = forms.ImageField(label="5", required=False)
    image6 = forms.ImageField(label="6", required=False)
    image7 = forms.ImageField(label="7", required=False)
    image8 = forms.ImageField(label="8", required=False)
    image9 = forms.ImageField(label="9", required=False)
    image10 = forms.ImageField(label="10", required=False)


    class Meta:
        model = Upload
        fields = ('hallname', 'description', 'type',
                  'town', 'availability', 'price', 'landlord', 'phone', 'image1', 'image2', 'image3', 'image4', )









'''
class UploadFileForm(forms.Form):
    hallname = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500)
    type = forms.CharField(max_length=100)
    town = forms.CharField(max_length=100)
    price = forms.PositiveIntegerField("Price")
    landlord_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    phone_number = forms.CharField(max_length=100)

class FileFieldForm(forms.Form):
    file_field = forms.ImageField(widget=forms.ClearableFileInput
    (attrs={'multiple': True}))
    
'''

