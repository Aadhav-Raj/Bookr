from django.contrib import admin

# Import your models here
from .models import Book,Publisher, Contributor, Review,BookContributor

# Register your models with the admin site
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Contributor)
admin.site.register(BookContributor)
admin.site.register(Review)
