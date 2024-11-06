from django import forms
from .models import Book,Publisher,Review

class SearchForm(forms.Form):
    search = forms.CharField(required=False,min_length=3)
    search_in = forms.ChoiceField(required=False,
                                  choices=(
                                      ("title", "Title"),
                                      ("contributor", "Contributor")
                                  ))
"""
class PublisherForm(forms.Form):
    name=forms.CharField(max_length=50)
    website=forms.URLField()
    email=forms.EmailField()
"""
class PublisherForm(forms.ModelForm):
    class Meta:
        model=Publisher
        fields="__all__"

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        exclude=["date_edited","book"]
    #rating=forms.IntegerField(min_value=0,max_value=5)

class BookMediaForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=["cover","sample"]
