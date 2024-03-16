from django import forms
from .models import Publisher,Review

class SearchForm(forms.Form):
    search = forms.CharField(required=False)
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
        exclude=["data_edited","book"]
    rating=forms.IntegerField(min_value=0,max_value=5)
