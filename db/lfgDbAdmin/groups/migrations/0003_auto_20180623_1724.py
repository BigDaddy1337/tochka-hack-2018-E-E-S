# Generated by Django 2.0.6 on 2018-06-23 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20180623_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel_id', models.TextField(max_length=512)),
                ('name', models.TextField(max_length=512)),
                ('l_name', models.TextField(max_length=512)),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.TextField(max_length=512),
        ),
        migrations.AddField(
            model_name='person',
            name='cur_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='groups.Group'),
        ),
        migrations.AddField(
            model_name='person',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='groups.PersonsType'),
        ),
    ]
