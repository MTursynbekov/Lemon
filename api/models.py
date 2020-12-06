from datetime import date

from django.db import models

MEN_WOMEN_KIDS_CHOICES = (
    ('M', 'MEN'),
    ('W', 'WOMEN'),
    ('G', 'GIRLS'),
    ('B', 'BOYS'),
    ('N', 'NEWBORNS'),
)

MEN = 'M'
WOMEN = 'W'
GIRLS = 'G'
BOYS = 'B'
NEWBORNS = 'N'


class ClothesCategory(models.Model):
    class Meta:
        verbose_name = "Категория одежды"
        verbose_name_plural = "Категории одежды"

    name = models.CharField(max_length=300)
    men_women_kids = models.CharField(max_length=1,
                                      choices=MEN_WOMEN_KIDS_CHOICES,
                                      default=WOMEN)

    def __str__(self):
        return f'{self.name}'


class ShoesCategory(models.Model):
    class Meta:
        verbose_name = "Категория обуви"
        verbose_name_plural = "Категории обуви"

    name = models.CharField(max_length=300)
    men_women_kids = models.CharField(max_length=1,
                                      choices=MEN_WOMEN_KIDS_CHOICES,
                                      default=WOMEN)

    def __str__(self):
        return f'{self.name}'


class AccessoriesCategory(models.Model):
    class Meta:
        verbose_name = "Категория аксессуаров"
        verbose_name_plural = "Категории аксессуаров"

    name = models.CharField(max_length=300)
    men_women_kids = models.CharField(max_length=1,
                                      choices=MEN_WOMEN_KIDS_CHOICES,
                                      default=WOMEN)

    def __str__(self):
        return f'{self.name}'


class Sport(models.Model):
    class Meta:
        verbose_name = "Вид спорта"
        verbose_name_plural = "Виды спорта"

    name = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name}'


class Brand(models.Model):
    class Meta:
        verbose_name = "Брэнд"
        verbose_name_plural = "Брэнды"

    name = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name}'


class Store(models.Model):
    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"

    name = models.CharField(max_length=100, verbose_name="название магазина")
    address = models.TextField(verbose_name="адрес магазина")
    brand = models.ForeignKey(Brand,
                              on_delete=models.CASCADE,
                              related_name="stores",
                              verbose_name="брэнд",
                              blank=True,
                              null=True)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    name = models.CharField(max_length=300, verbose_name="Название продукта")
    price = models.FloatField(verbose_name="Цена продукта")
    in_stock = models.BooleanField(default=False, verbose_name='Есть в наличии?')
    composition = models.CharField(max_length=300, verbose_name="Состав продукта")
    colour = models.CharField(max_length=100, verbose_name="Цвет продукта")
    description = models.TextField(verbose_name="Описание продукта", default="")
    country = models.CharField(max_length=100, verbose_name="Страна производителя")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    ends_date = models.DateField(default=date.today, verbose_name="Время окончания скидки")
    is_sport = models.BooleanField(default=False, verbose_name="Это продукт для спорта?")
    city = models.CharField(max_length=100, verbose_name="В каком городе продукт?")
    sport = models.ForeignKey(Sport,
                              on_delete=models.CASCADE,
                              related_name="products",
                              verbose_name="Вид спорта",
                              blank=True,
                              null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="brand", verbose_name="Брэнд продукта")
    stores = models.ManyToManyField(Store,
                                    related_name="products",
                                    verbose_name="магазины",
                                    blank=True,
                                    null=True)


class ProductImage(models.Model):
    class Meta:
        verbose_name = "Картинка продукта"
        verbose_name_plural = "Картинки продукта"

    src = models.ImageField(upload_to='product_images/')
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name="images",
                                verbose_name="Продукт",
                                blank=True,
                                null=True)

    def __str__(self):
        return f'product: {self.product}'


class Clothes(Product):
    class Meta:
        verbose_name = "Одежда"
        verbose_name_plural = "Одежда"

    category = models.ForeignKey(ClothesCategory,
                                 on_delete=models.CASCADE,
                                 related_name="products",
                                 verbose_name="Категория одежды",
                                 blank=True,
                                 null=True)
    size = models.CharField(max_length=10, verbose_name="Размер одежды")
    size_digit = models.PositiveIntegerField(verbose_name="Размер одежды в цифрах")

    def __str__(self):
        return f'name: {self.name}, category: {self.category}, brand: {self.brand}'


class Shoes(Product):
    class Meta:
        verbose_name = "Обувь"
        verbose_name_plural = "Обуви"

    category = models.ForeignKey(ShoesCategory,
                                 on_delete=models.CASCADE,
                                 related_name="products",
                                 verbose_name="Категория обуви",
                                 blank=True,
                                 null=True)
    size = models.FloatField(verbose_name="Размер обуви")

    def __str__(self):
        return f'name: {self.name},  category: {self.category},  brand: {self.brand}'


class Accessories(Product):
    class Meta:
        verbose_name_plural = "Аксессуары"

    category = models.ForeignKey(AccessoriesCategory,
                                 on_delete=models.CASCADE,
                                 related_name="products",
                                 verbose_name="Категория аксессуара",
                                 blank=True,
                                 null=True)

    def __str__(self):
        return f'name: {self.name}, category: {self.category}, brand: {self.brand}'


class SpecialOffer(models.Model):
    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"

    src = models.ImageField(upload_to="special_offer_images")
    begins_date = models.DateField(default=date.today, verbose_name="Дата начало акции")
    ends_date = models.DateField(default=date.today, verbose_name="Дата окончания акции")
    brand = models.ForeignKey(Brand,
                              on_delete=models.CASCADE,
                              related_name="special_offers",
                              verbose_name="брэнд",
                              blank=True,
                              null=True)

    def __str__(self):
        return f'brand: {self.brand}'
