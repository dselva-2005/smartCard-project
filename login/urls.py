from django.urls import path,include
from .views import Home

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('accounts/',include('django.contrib.auth.urls'))
]
