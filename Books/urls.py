from django.urls import path
from Books import views as v

urlpatterns = [
    path('sell/', v.sell, name='sell'),
    path('buy/', v.buy, name='buy'),
    path('donate/', v.donate, name='donate'),
]
