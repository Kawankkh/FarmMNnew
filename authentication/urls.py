from django.contrib import admin
from django.urls import path, include
from authentication import views
urlpatterns = [
    path('homepage', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('', views.signin, name='signin'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('dashborad', views.dashborad, name='dashborad'),
    path('customer', views.customer, name='customer'),
    path('farmmer', views.farmmer, name='farmmer'),
    path('farmmerdetail', views.farmmerdetail, name='farmmerdetail'),
    path('stock_item', views.stock_item, name='stock_item'),
]
