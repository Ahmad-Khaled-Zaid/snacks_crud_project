# Generated by Django 4.0.6 on 2022-08-02 05:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snacks', '0003_remove_snack_register_model_alter_snack_purchaser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Snack',
            new_name='Snack1',
        ),
    ]
