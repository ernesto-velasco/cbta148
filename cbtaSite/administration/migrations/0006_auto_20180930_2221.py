# Generated by Django 2.1.1 on 2018-10-01 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0005_propertyfile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basic_info',
            old_name='direction',
            new_name='address',
        ),
    ]