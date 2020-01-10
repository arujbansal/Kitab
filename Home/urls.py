from django.urls import path
from Home import views as v

urlpatterns = [
    path('', v.home, name='home'),
]
