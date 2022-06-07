from django.shortcuts import render,redirect
from books.models import *


def dashboard(request):
    return render(request,'dashboard.html')

def book(request):
    book = Book.objects.all()

    context = {
        'book':book
    }
    return render(request,'book.html',context)

def delete(request,id):
    book = Book.objects.get(id=id)
    book.delete()


    return redirect('book')

