# Generated by Django 2.1.1 on 2018-10-04 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20181003_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='banner_image',
            field=models.ImageField(blank=True, null=True, upload_to='assets/post_image/'),
        ),
    ]
