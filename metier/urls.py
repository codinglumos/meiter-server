from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from metierapi.views import register_user, login_user
from metierapi.views import CustomerView
from metierapi.views import CreatorView
from metierapi.views import ServiceView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'customers', CustomerView, 'customer')
router.register(r'creators', CreatorView, 'creator')
router.register(r'services', ServiceView, 'service')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]