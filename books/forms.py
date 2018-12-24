from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class DeleteConfirmForm(forms.Form):
    check = forms.BooleanField(label='你確認要刪除嗎?')