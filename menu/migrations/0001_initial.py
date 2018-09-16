# Generated by Django 2.1.1 on 2018-09-12 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название блюда')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Цена')),
                ('rating', models.IntegerField(null=True, verbose_name='Рейтинг')),
                ('vegan', models.BooleanField(verbose_name='Вегетерианкое')),
                ('allergens', models.CharField(max_length=64, null=True, verbose_name='Аллергены')),
            ],
            options={
                'verbose_name': 'Блюдо',
                'verbose_name_plural': 'Блюда',
                'ordering': ('-rating', '-id'),
            },
        ),
    ]