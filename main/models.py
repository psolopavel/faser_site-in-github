from datetime import date

from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField('Категория', max_length=80)
    description = models.TextField('описание')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категорий'

class Salesman(models.Model):
    name = models.CharField('имя', max_length=200)
    age = models.PositiveSmallIntegerField('возраст', default=18)
    description = models.TextField('описание')
    image = models.ImageField('Изоброжение',upload_to='salesman/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продовец'
        verbose_name_plural = 'Продовци'

class Shop_name(models.Model):
    name = models.CharField('имя', max_length=80)
    description = models.TextField('описание')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'название магазина'
        verbose_name_plural = 'название магазинов'

class Product(models.Model):
    title = models.CharField('назваие продукта', max_length=150)
    descriptin = models.TextField('описание')
    price = models.PositiveIntegerField('цена', default=0, help_text='указивать в $')
    poster = models.ImageField('изоброжение', upload_to='product/')
    salesman = models.ManyToManyField(Salesman,verbose_name='продовец', related_name='salesman')
    category = models.ManyToManyField(Category, verbose_name='категорий')
    Shop_name = models.ForeignKey(Shop_name,verbose_name='название магазина', on_delete=models.SET_NULL,null=True)
    number = models.PositiveSmallIntegerField('номер телефона')
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField('черновик', default=False)

    def __str__(self):
        return self.title

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    def get_absolute_url(self):
        return reverse('product_url',kwargs={'slug' : self.url})

    class Meta:
        verbose_name = 'прдукт'
        verbose_name_plural = 'прдукти'



class product_Shorts(models.Model):

    title = models.CharField('название', max_length=100)
    description = models.TextField('описание')
    image = models.ImageField('изоброжение', upload_to='product_shorts/')
    product = models.ForeignKey(Product,verbose_name='продукт', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'кадри продукта'
        verbose_name_plural = 'кадри продукта'


class Rating_star(models.Model):
    value = models.PositiveSmallIntegerField('значение', default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = 'звезда рейтинга'
        verbose_name_plural = 'звезди рейтинга'
        ordering = ['-value']

class Rating(models.Model):
    ip = models.CharField('IP адрес',max_length=15)
    star = models.ForeignKey(Rating_star,on_delete=models.CASCADE, verbose_name='зведа')
    product = models.ForeignKey(Product,on_delete=models.CASCADE, verbose_name='фильм')

    def __str__(self):
        return f'{self.star} - {self.product}'

    class Meta:
        verbose_name = 'рейтинг'
        verbose_name_plural = 'рейтинги'
# Create your models here.

class Reviews(models.Model):

    email = models.EmailField()
    name = models.CharField('имя', max_length=100)
    text = models.TextField('сообщение', max_length=5000)
    parent = models.ForeignKey('self', verbose_name='родитель', on_delete=models.SET_NULL, blank=True, null=True)

    product = models.ForeignKey(Product,verbose_name='продукт', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.product}'

    class Meta:
        verbose_name = 'Отзив'
        verbose_name_plural = 'Отзиви'


class Purchase(models.Model):
    room = models.PositiveSmallIntegerField('номер')
    product = models.ForeignKey(Product, verbose_name='продукт',on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.room} - {self.product}'

    class Meta:
        verbose_name = 'покупка'
        verbose_name_plural = 'покупки'
