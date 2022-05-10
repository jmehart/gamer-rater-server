from rest_framework import routers
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from raterapp.views.auth import login_user, register_user
from raterapp.views.category import CategoryView
from raterapp.views.game import GameView
from raterapp.views.game_category import GameCategoryView
from raterapp.views.gamer import GamerView
from raterapp.views.review import ReviewView
from raterapp.views.rating import RatingView
from raterapp.views.image import ImageView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'games', GameView, 'game')
router.register(r'categories', CategoryView, 'category')
router.register(r'reviews', ReviewView, 'review')
router.register(r'ratings', RatingView, 'rating')
router.register(r'images', ImageView, 'image')
router.register(r'gamers', GamerView, 'gamer')
router.register(r'game_categories', GameCategoryView, 'game_category')


urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)