from django.shortcuts import render

from .models import Book


# Create your views here.


def index(request):
    return render(request, "books/index.html", {
        "books": Book.objects.all()
    })


def book(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, "books/book.html", {
        "book": book
    })
