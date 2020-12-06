# from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ClothesCategory, ShoesCategory, AccessoriesCategory, Brand, Sport, Clothes, Shoes, \
    Accessories, SpecialOffer
from .serializers import ClothesCategorySerializer, ShoesCategorySerializer, \
    AccessoriesCategorySerializer, BrandSerializer, SportSerializer, ClothesSerializer, ShoesSerializer, \
    AccessoriesSerializer, SpecialOfferSerializer

'''
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
'''


class ClothesCategoriesViewSet(viewsets.ModelViewSet):
    queryset = ClothesCategory.objects.all()
    serializer_class = ClothesCategorySerializer

    @action(detail=True, url_path='products')
    def get_category_products(self, request, pk=None):
        category_products = Clothes.objects.filter(category_id=pk)
        serializer = ClothesSerializer(category_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ShoesCategoriesViewSet(viewsets.ModelViewSet):
    queryset = ShoesCategory.objects.all()
    serializer_class = ShoesCategorySerializer

    @action(detail=True, url_path='products')
    def get_category_products(self, request, pk=None):
        category_products = Shoes.objects.filter(category_id=pk)
        serializer = ShoesSerializer(category_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AccessoriesCategoriesViewSet(viewsets.ModelViewSet):
    queryset = AccessoriesCategory.objects.all()
    serializer_class = AccessoriesCategorySerializer

    @action(detail=True, url_path='products')
    def get_category_products(self, request, pk=None):
        category_products = Accessories.objects.filter(category_id=pk)
        serializer = AccessoriesSerializer(category_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SportsViewSet(viewsets.ModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer


class BrandsViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    @action(detail=True, url_path='special_offers')
    def get_brands_special_offers(self, request, pk=None):
        brands_special_offers = SpecialOffer.objects.filter(brand_id=pk)
        serializer = SpecialOfferSerializer(brands_special_offers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ClothesViewSet(viewsets.ModelViewSet):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer


class ShoesViewSet(viewsets.ModelViewSet):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer


class AccessoriesViewSet(viewsets.ModelViewSet):
    queryset = Accessories.objects.all()
    serializer_class = AccessoriesSerializer


class SpecialOffersViewSet(viewsets.ModelViewSet):
    queryset = SpecialOffer.objects.all()
    serializer_class = SpecialOfferSerializer
