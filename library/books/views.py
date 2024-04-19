from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login
from .models import Students, Book , Borrower
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    
    book = Book.objects.all()
    return render(request,"books/home.html",{
        "book":book, 
    })

@login_required(login_url="login")
def addstudents(request):
    if request.method == 'POST':
        name = request.POST['name']
        branch = request.POST['branch']
        rollno = request.POST['rollno']
        phonenumber = request.POST['phonenumber']
        photo = request.FILES.get('photo')
         

        new_student = Students(
            name = name,
            branch = branch,
            rollno = rollno,
            phonenumber = phonenumber,
            photo = photo,
        )

        new_student.save()

    return render(request,"books/addstudents.html")

@login_required(login_url="login")
def admin(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        description = request.POST['description']
        category = request.POST['category']
        total_copies = request.POST['copies']
        available_copies = request.POST['availcopies']
        image = request.POST['image']

        new_book = Book(
            title = title,
            author = author, 
            description = description,
            category = category,
            total_copies  = total_copies,
            available_copies = available_copies,
            image = image,

            )
        
        new_book.save()
    return render(request,"books/admin.html")

#def login(request):
#    return render(request,"books/login.html")

@login_required(login_url="login")
def students(request):
    students = Students.objects.all()
   
    return render(request,"books/students.html",{
        "students":students,
        
    })

@login_required(login_url="login")
def borrow_book(request):
    print("home")
    if request.method == 'POST':
        name = request.POST['name']
        branch = request.POST['branch']
        rollno = request.POST['rollno']
        phonenumber = request.POST['phonenumber']
        title = request.POST['bookname']
        print("success")
        student, _ = Students.objects.get_or_create(
            name=name,
            branch=branch,
            rollno=rollno,
        )

        book = get_object_or_404(Book, title=title)
     
        if book.available_copies > 0:
            borrowed_book = Borrower(student=student, book=book)
            borrowed_book.save()

            book.available_copies -= 1
            book.save()

    borrow = Borrower.objects.all()
    return render(request, "books/borrow.html", {
        "borrow": borrow,
    })

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            #login(request, user)
            # Replace 'desired_page' with the URL name or path of the desired page
            return redirect("admin")
        else:
            return HttpResponse("incorrect")#render(request, 'login.html', {'error_msg': 'Invalid username and/or password'})
    else:
        return render(request, 'books/login.html')


def bookinfo(request,book_title):
    bookinfo = Book.objects.get(title = book_title)
    return render(request, "books/bookinfo.html",{
        "bookinfo":bookinfo,
    })
 