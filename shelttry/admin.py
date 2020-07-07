from django.contrib import admin
from .models import  Houses, Post, Images, Upload, Test, TestImages

# Register your models here.

admin.site.register(Houses)
admin.site.register(Post)
admin.site.register(Upload)
admin.site.register(Test)
admin.site.register(TestImages)
