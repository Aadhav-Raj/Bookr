from django.contrib import admin
from django.shortcuts import render

# Import your models here
from .models import Book,Publisher, Contributor, Review,BookContributor

# Register your models with the admin site
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Contributor)
admin.site.register(BookContributor)
admin.site.register(Review)


# myapp/admin.py

from django.contrib import admin

"""

def my_custom_view(request):
    # perform some custom action
    # ...
    return render(request, 'admin/admin_profile.html')

# register the custom view
admin.site.register_view('customview/', view=my_custom_view, name='My Custom View')

"""
