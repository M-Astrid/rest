# Generated by Django 2.1.1 on 2018-09-22 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20180922_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='img',
            field=models.FileField(default='uploads/chicken.svg', upload_to='uploads/'),
        ),
    ]
