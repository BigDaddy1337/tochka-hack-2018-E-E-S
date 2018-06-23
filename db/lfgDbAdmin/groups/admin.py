from django.contrib import admin
from .models import Group, PersonsType, Person, Section

admin.site.register(Group)
admin.site.register(PersonsType)
admin.site.register(Person)
admin.site.register(Section)