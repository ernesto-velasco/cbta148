# Generated by Django 2.1.1 on 2018-10-05 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20181004_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=models.ImageField(upload_to='posts/%Y/%m/%d/images'),
        ),
    ]