# Generated by Django 4.0.6 on 2022-08-01 18:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snacks', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Snacks',
            new_name='Snack',
        ),
    ]
