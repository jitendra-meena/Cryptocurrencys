# Generated by Django 3.2.14 on 2022-07-14 17:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BCTAlert',
            new_name='BTCAlert',
        ),
    ]
