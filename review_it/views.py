from django.shortcuts import render
from django.contrib.auth import authenticate, login , logout
from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from .models import Book,Review
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request , 'home.html')

def logout_(request):
    logout(request)
    return render(request , 'home.html')

def login_page(request):
    return render(request,'login.html')

def login_auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request , user)
        return render(request , 'login_home.html')
    else:
        return render(request , 'login_fail.html')

def signup(request):
    return render(request , 'signup.html')

def add_user(request):
    """new_user = User()
    new_user.username = request.POST['username']
    new_user.password = request.POST['password']
    new_user.first_name = request.POST['first_name']
    new_user.last_name = request.POST['last_name']
    new_user.email = request.POST['email']
    new_user.save()"""
    return render(request , 'user_added.html')

@login_required(login_url='{% review_it:login_page %}')
def write_review(request):
    return render(request , 'write_review.html')


def add_review(request):
    """new_book = Book()
    new_book.title=request.POST['title']
    new_book.auther=request.POST['author']
    new_book.publisher=request.POST['publisher']
    new_book.number_of_reviews = 1
    new_book.average_rating = request.POST['star_rating']
    new_book.save()"""
    new_review=Review()
    new_review.review = request.POST['review']
    new_review.star_rating = request.POST['star_rating']
    new_review.review_by = User.objects.get(id=request.user.id)
    new_review.book= request.POST['title']
    #check_book = Book.objects.filter(title=new_book.title)
    #if check_book==[]:
    #a=check_book[0]
   # new_review.book = request.POST['title']
    #else:
     #   check_book[0].number_of_reviews += 1
      #  check_book[0].average_rating = 3
        #check_book[0].average_rating = (((check_book[0].average_rating)* (int(check_book[0].number_of_reviews)-1))+(new_review.star_rating))/(check_book[0].number_of_reviews)
       # check_book[0].save()
        #new_review.review_of = Book.objects.get(id=check_book[0].id)
    new_review.save()
    return render(request , 'login_home.html')

def search(request):
    svalue = request.POST['svalue']
    all_reviews=Review.objects.filter(book=svalue).order_by('-datetime')
    return render(request , 'results.html' , {'all_reviews':all_reviews})