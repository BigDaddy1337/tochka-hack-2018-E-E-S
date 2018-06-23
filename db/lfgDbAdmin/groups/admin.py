from django.contrib import admin
from .models import Group, PersonsType, Person

admin.site.register(Group)
admin.site.register(PersonsType)
admin.site.register(Person)