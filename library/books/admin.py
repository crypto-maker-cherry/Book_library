from django.contrib import admin
from .models import Students, Book , Borrower

# Register your models here.

admin.site.register(Students)
admin.site.register(Book)
admin.site.register(Borrower)