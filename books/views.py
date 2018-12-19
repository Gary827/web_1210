from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Book
from .forms import BookForm

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
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,'新增成功')
        return redirect('books-index')

        
            
           
    

        # name = request.POST.get('name')
        # price = request.POST.get('price')
        # introduction = request.POST.get('introduction')

        

    return render(request, 'books/add.html',{'form':form})