from django.shortcuts import render, redirect
from .models import Destination
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse


# Create your views here.
def post(request):

    if request.method == 'POST':
        hallname = request.POST['hall_name']
        description = request.POST['description']
        area = request.POST['area']
        type = request.POST['type']
        landlord_name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        document1 = request.POST['myfile1']
        document2 = request.POST['myfile2']
        document3 = request.POST['myfile3']
        document4 = request.POST['myfile4']

        house = House(hallname=hallname, description=description, area=area, type=type,
                        landlord_name=landlord_name, email=email, phone_number=phone_number,
                        document1=document1, document2=document2,
                        document3=document3,  document4=document4)

        if house.is_valid():
            house.save()
            return redirect('success')

    else:
        return render(request, 'post.html')

'''
def success(request):
    return HttpResponse('successfully uploaded')

'''
def subscribe(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']


        house = Subscribe(name=name, email=email)
        house.save()
        return redirect('/')

    else:
        return render(request, 'index.html')


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html',
                      {'uploaded_file_url': uploaded_file_url})
    return render(request, 'core/simple_upload.html')

def destinations(request):

    dest1 = Destination()
    dest1.name = 'Mariam'
    return render(request, 'destinations.html', {'dest1': dest1})

def about(request):
    return render(request, 'about.html')

