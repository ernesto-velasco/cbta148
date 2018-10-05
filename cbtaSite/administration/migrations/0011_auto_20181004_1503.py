# Generated by Django 2.1.1 on 2018-10-04 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0010_auto_20181003_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='slider/%Y/%m/%d/files'),
        ),
        migrations.AlterField(
            model_name='pagefile',
            name='file',
            field=models.FileField(upload_to='page/%Y/%m/%d/files'),
        ),
        migrations.AlterField(
            model_name='pageimage',
            name='image',
            field=models.ImageField(upload_to='page/%Y/%m/%d/images'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to='slider/%Y/%m/%d/images'),
        ),
    ]
