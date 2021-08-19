from django.urls import path

from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('order/', views.Order.as_view(), name='order'),
    path('ordered/', views.orderList, name='ordered'),
    path('profile/',  views.Profile.as_view(), name='profile'),

]