from django.urls import path

from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('order/', views.Order.as_view(), name='order'),
    path('ordered/', views.OrderList, name='ordered'),
    path('profile/',  views.UploadFile, name='profile'),
    
]