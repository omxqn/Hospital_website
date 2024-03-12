from django.urls import path
from . import views


urlpatterns=[
path('', views.pharamacy_dashboard, name='pharamacy_dashboard'),
path('pharamacy_devices/', views.pharamacy_devices, name='pharamacy_devices'),
path('pharamacy_medicine_stock/', views.pharamacy_medicine_stock, name='pharamacy_medicine_stock'),
path('add_medicine/', views.add_medicine, name='add_medicine'),
path('edit_medicine/<int:id>', views.edit_medicine, name='edit_medicine'),
path('pharamacy_patient_prescription/', views.pharamacy_patient_prescription, name='pharamacy_patient_prescription'),
path('prescription_details/<int:id>', views.prescription_details, name='prescription_details'),

path('pharamacy_profile', views.pharamacy_profile, name='pharamacy_profile'),


 path('cart/add/<int:product_id>', views.add_cart, name='add_cart'),
 path('cart', views.cart_detail, name='cart_detail'),
 path('add_to_cart', views.add_to_cart, name='add_to_cart'),
 path('cart/remove/<int:product_id>', views.cart_remove, name='cart_remove'),

 path('thanks_page/<int:order_id>', views.thanks_page, name='thanks_page'),












]