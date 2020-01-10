from django.shortcuts import render, redirect
from Books.forms import BookForm
from django.contrib import messages
from Books.models import Book


def sell(request):
    if request.method == "GET":
        form = BookForm()
    else:
        form = BookForm(request.POST, request.FILES)
        form.instance.rel_user = request.user
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully added!")
            return redirect('sell')
        else:
            messages.error(request, "Please fill in all the fields.")
    return render(request, 'Books/sell.html', {"form": form})


def buy(request):
    available_books = Book.objects.all()
    first_3 = available_books[0:2]
    return render(request, 'Books/buy.html', {"books": available_books, "first_3": first_3})
