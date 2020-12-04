from django.urls import path

from . import views

urlpatterns = [
    path('house_price_data/query_id=<int:query_id>/', views.house_price_data, name='query_id'),
    path('index/', views.index)
]