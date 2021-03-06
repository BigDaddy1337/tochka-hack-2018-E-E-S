# Generated by Django 2.0.6 on 2018-06-23 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_auto_20180623_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='section',
            field=models.TextField(blank=True, max_length=512),
        ),
        migrations.AddField(
            model_name='person',
            name='section',
            field=models.TextField(blank=True, max_length=512),
        ),
        migrations.AddField(
            model_name='personstype',
            name='section',
            field=models.TextField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='group',
            name='persons',
            field=models.ManyToManyField(blank=True, to='groups.PersonsType'),
        ),
        migrations.AlterField(
            model_name='group',
            name='status',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='personstype',
            name='groups',
            field=models.ManyToManyField(blank=True, to='groups.Group'),
        ),
    ]
