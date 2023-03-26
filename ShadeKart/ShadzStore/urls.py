from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='storeIndex'),
    path('about/', views.about, name='AboutUs'),
    path('contact/', views.contact, name='ContactUs'),
    path('productView/<int:my_id>', views.productView, name='ProductView'),
    path('login/', views.login, name='Login'),
    path('userHomepage/', views.login, name='User Homepage'),
    path('signup/', views.signUp, name='Sign Up'),
    path('search/', views.search, name='Search'),
    path('trackProduct/', views.tracker, name='Track'),
    path('checkout/', views.checkout, name='Checkout'),
    path('checkout/orderConfirm/', views.orderConfirmation, name='Confirm order'),
]
