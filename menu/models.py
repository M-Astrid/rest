#coding: utf-8

from django.db import models

# Create your models here.

class Dish(models.Model):
    title = models.CharField(verbose_name=u'Название блюда', max_length=255)
    price = models.DecimalField(verbose_name=u'Цена', max_digits=6, decimal_places=2)
    rating = models.IntegerField(verbose_name=u'Рейтинг', default=0, null=True)
    vegan = models.BooleanField(verbose_name=u'Вегетерианкое')
    allergens = models.CharField(verbose_name=u'Аллергены', max_length=64)
    img = models.FileField(upload_to='uploads/', default='uploads/chicken.svg')

    def __unicode__(self):
        return self.title()

    class Meta:
        verbose_name = u'Блюдо'
        verbose_name_plural = u'Блюда'
        ordering = ('-rating', '-id')

