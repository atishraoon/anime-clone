# Generated by Django 5.1.4 on 2024-12-22 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_remove_animelist_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='animelist',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
