from django.contrib import admin
from .models import State, City, Locality

admin.site.register(State)
admin.site.register(City)
admin.site.register(Locality)