# Generated by Django 2.1.1 on 2018-09-22 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20180922_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='img',
            field=models.FileField(default='menu/img/raw_meat.svg', upload_to='uploads/'),
        ),
    ]
