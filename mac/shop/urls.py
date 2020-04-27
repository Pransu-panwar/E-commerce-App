
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('about/', views.about, name="Aboutus"),
    path('contact/', views.contact, name="Contactus"),
    path('tracker/', views.tracker, name="Tracker"),
    path('search', views.search, name="Search"),
    path('products/<int:myid>', views.productview, name="Productview"),
    path('checkout', views.checkout, name="Checkout")
]