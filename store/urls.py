from django.urls import path
from . import views

app_name='store'
urlpatterns = [
    path('', views.index, name='index'),
    path('product/pay/paypal/<int:pk>', views.make_pay_paypal, name='make_pay_paypal'),
    path('product/paypal/success/<int:pk>', views.paypal_success, name='paypal_success'),
    path('product/paypal/cancel', views.paypal_cancel, name='paypal_cancel'),
    path('bought', views.bought, name='bought'),
    path('product/payed/detail/<int:pk>', views.detail_pay, name='detail_pay'),
    path('agregar/', views.agregar, name='agregar'),
    path('modificar/<int:pk>', views.modificar, name='modificar'),
    path('product/<int:pk>',views.DetailView.as_view(), name='detail'),
    path('product/<slug:url_clean>',views.DetailView.as_view(), name='detail'),
    path('product/<int:pk>/<slug:url_clean>',views.DetailView.as_view(), name='detail'),
]
