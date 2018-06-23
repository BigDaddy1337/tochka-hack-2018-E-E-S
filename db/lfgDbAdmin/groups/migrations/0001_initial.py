# Generated by Django 2.0.6 on 2018-06-23 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=500)),
                ('status', models.IntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(max_length=1024)),
                ('groups', models.ManyToManyField(to='groups.Group')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='persons',
            field=models.ManyToManyField(to='groups.PersonsType'),
        ),
    ]