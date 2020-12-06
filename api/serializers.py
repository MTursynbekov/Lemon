from rest_framework import serializers
from .models import ClothesCategory, ShoesCategory, AccessoriesCategory, Brand, Sport, Store, ProductImage, \
    Clothes, Shoes, Accessories, SpecialOffer


'''
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        password = {'password': {'write_only': True, 'required': True}}
'''


class ClothesCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothesCategory
        fields = '__all__'


class ShoesCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoesCategory
        fields = '__all__'


class AccessoriesCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessoriesCategory
        fields = '__all__'


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = '__all__'


class SpecialOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialOffer
        fields = ('id', 'src')


class BrandSerializer(serializers.ModelSerializer):
    special_offer = SpecialOfferSerializer(many=True, read_only=True)

    class Meta:
        model = Brand
        fields = '__all__'


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'src')


'''
class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    images = ProductImageSerializer(many=True)
    sport = SportSerializer()
    store = StoreSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'
'''


class ClothesSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    images = ProductImageSerializer(many=True)
    sport = SportSerializer()
    stores = StoreSerializer(many=True)
    category = ClothesCategorySerializer()

    class Meta:
        model = Clothes
        fields = '__all__'


class ShoesSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    images = ProductImageSerializer(many=True)
    sport = SportSerializer()
    store = StoreSerializer(many=True)
    category = ShoesCategorySerializer()

    class Meta:
        model = Shoes
        fields = '__all__'


class AccessoriesSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    images = ProductImageSerializer(many=True)
    sport = SportSerializer()
    store = StoreSerializer(many=True)
    category = AccessoriesCategorySerializer()

    class Meta:
        model = Accessories
        fields = '__all__'



