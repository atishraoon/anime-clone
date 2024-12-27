# Generated by Django 5.1.4 on 2024-12-22 07:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_remove_animelist_name_animelist_anime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animelist',
            name='anime',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.anime'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(upload_to='profile_pic/'),
        ),
    ]
