from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig



class BookrAdminConfig(AdminConfig):
    default_site = 'bbbookr_admin.admin.BookrAdmin'


"""
class BookrAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bbbookr_admin'
"""
