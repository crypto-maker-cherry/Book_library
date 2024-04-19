from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length= 70)
    branch = models.CharField(max_length= 70)
    rollno = models.CharField(max_length= 70) 
    phonenumber = models.PositiveIntegerField() 
    

    def __str__(self):
        return f"{self.name}"
    

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100)
    total_copies = models.IntegerField()
    available_copies = models.IntegerField(blank=True, null=True)
    image=models.ImageField(blank=True, null=True, upload_to='book_image')

    def __str__(self):
        return f"{self.title}"
    

class Borrower(models.Model):
    student = models.ForeignKey('Students', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    issue_date = models.DateTimeField(default=date.today())
    return_date = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.student.name+" borrowed "+self.book.title