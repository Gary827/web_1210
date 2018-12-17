from django.shortcuts import render, get_object_or_404

from .models import Book


def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html',{'books':books})


def show(request, pk):
    # try:
    #     book = Book.objects.get(pk=pk)
    # except Exception:
    #     raise HTTP404
    book = get_object_or_404(book, pk=pk)

    return render(request, 'books/show.html',{
        'book': book
    })

def add(request):
    return render(request, 'books/add.html')