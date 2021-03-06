from django.db import models

class Group(models.Model):
    name = models.TextField(max_length=256)
    description = models.TextField(max_length=512, blank = True)
    status = models.IntegerField(blank = True)
    section = models.ForeignKey('Section', blank = True, null = True, on_delete=models.SET_NULL)
    persons = models.ManyToManyField('PersonsType', blank = True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PersonsType(models.Model):
    type = models.TextField(max_length=1024)
    groups = models.ManyToManyField('Group', blank = True)
    section = models.ManyToManyField('Section', blank = True)

    def __str__(self):
        return self.type

class Person(models.Model):
    tel_id = models.TextField(max_length=256)
    name = models.TextField(max_length=256)
    l_name = models.TextField(max_length=256)
    type = models.ForeignKey('PersonsType', blank = True, null = True, on_delete=models.SET_NULL)
    section = models.ForeignKey('Section', blank = True, null = True, on_delete=models.SET_NULL)
    status = models.IntegerField()
    cur_group = models.ForeignKey('Group', blank = True, null = True, on_delete=models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + ' ' + self.l_name

class Section(models.Model):
    title = models.TextField(max_length=256)

    def __str__(self):
        return self.title