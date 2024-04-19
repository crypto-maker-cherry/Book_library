from django.urls import path 
from . import views 
from .views import login

urlpatterns = [
    path('',views.home  ),
    path('books', views.home ),
    path('home',views.home, name="home"),
    path('addstudents',views.addstudents, name="addstudents"),
    path('students',views.students, name="students"),
    path('admin',views.admin, name="admin"),
    path('login',views.login, name='login'),
    path('borrowers/', views.borrow_book, name='borrow'),
    path('book/<book_title>',views.bookinfo,name="bookinfo"),
]