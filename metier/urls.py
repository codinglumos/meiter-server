from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from metierapi.views import register_user, login_user
from metierapi.views.service_view import ServiceView
from metierapi.views.favorite_view import FavoriteView
from metierapi.views.user_view import MetierUserView
from metierapi.views.reaction_view import ReactionsView
from metierapi.views.comment_view import CommentView
from metierapi.views.metier_customerview import MetierCustomerView
from metierapi import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'favorites', FavoriteView, 'favorite')
router.register(r'metiercreators', MetierUserView, 'metiercreator')
router.register(r'metiercustomers', MetierCustomerView, 'metiercustomer')
router.register(r'reactions', ReactionsView, 'reaction')
router.register(r'comments', CommentView, 'comment')
router.register(r'services', ServiceView, 'service')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('services/<int:pk>/delete/', ServiceView.as_view({'delete': 'destroy'}), name='service-delete'),
    path('services/<int:pk>/update/', ServiceView.as_view({'patch': 'update'}), name='service-update'),
    path('services/', views.ServiceView.as_view({'get': 'list', 'post': 'create'}), name='service-list'),
    path('services/<int:pk>/', views.ServiceView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='service-detail'),
    path('services/<int:pk>/create_reaction/', views.ServiceView.as_view({'post': 'create_reaction'}), name='service-create-reaction'),
]