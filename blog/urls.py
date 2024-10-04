from django.urls import path
from .views import index, two

urlpatterns = [
    path('', index, name='index'),
    path('not_found/', two, name='404'),
]

# {% url 'portfolio_detail' portfolio.slug %}