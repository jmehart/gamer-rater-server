from rest_framework import routers
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from raterapp.views.auth import login_user, register_user
from raterapp.views.category import CategoryView
from raterapp.views.game import GameView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'games', GameView, 'game')
router.register(r'categories', CategoryView, 'category')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]