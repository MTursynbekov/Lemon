from rest_framework.routers import DefaultRouter
from .views import ClothesCategoriesViewSet, ShoesCategoriesViewSet, AccessoriesCategoriesViewSet, SportsViewSet, \
    ClothesViewSet, BrandsViewSet, ShoesViewSet, AccessoriesViewSet, SpecialOffersViewSet

router = DefaultRouter()
router.register(r'clothes_categories', ClothesCategoriesViewSet)
router.register(r'shoes_categories', ShoesCategoriesViewSet)
router.register(r'accessories_categories', AccessoriesCategoriesViewSet)
router.register(r'sports', SportsViewSet)
router.register(r'brands', BrandsViewSet)
router.register(r'clothes', ClothesViewSet)
router.register(r'shoes', ShoesViewSet)
router.register(r'accessories', AccessoriesViewSet)
router.register(r'special_offers', SpecialOffersViewSet)
# router.register(r'users', UserViewSet)
urlpatterns = router.urls
