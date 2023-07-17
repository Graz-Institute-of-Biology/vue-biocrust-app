import os

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "../djangorestapi/settings.py")
from django.conf import settings
settings.configure()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

from  models import Document

list = [f.name for f in Document._meta.get_fields()]
print('')