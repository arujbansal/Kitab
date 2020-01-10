from django.forms import ModelForm
from Books.models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['image', 'title', 'description', 'price', 'state', 'city', 'neighbourhood', 'phone']
