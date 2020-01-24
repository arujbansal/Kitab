from django.urls import path
from Payments import views

urlpatterns = [
    path("payment/", views.make_payment, name="Pay"),
    path("payment_check/", views.payment_notification, name="CheckPayment"),

]
