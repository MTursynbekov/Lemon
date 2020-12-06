from django.contrib import admin
from .models import ClothesCategory, ShoesCategory, AccessoriesCategory, Brand, Sport, Store, Product, ProductImage, \
    Clothes, Shoes, Accessories, SpecialOffer

# Register your models here.
admin.site.register(ClothesCategory)
admin.site.register(ShoesCategory)
admin.site.register(AccessoriesCategory)
admin.site.register(Sport)
admin.site.register(Brand)
admin.site.register(Store)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Clothes)
admin.site.register(Shoes)
admin.site.register(Accessories)
admin.site.register(SpecialOffer)

