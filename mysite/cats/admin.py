from django.contrib import admin

from .models import Breed
from .models import Cat

admin.site.register(Breed)
admin.site.register(Cat)
