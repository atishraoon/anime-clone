# Generated by Django 5.1.4 on 2024-12-22 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_animelist_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animelist',
            name='name',
        ),
    ]
