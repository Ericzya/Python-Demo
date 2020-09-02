from django.urls import path

from . import views

urlpatterns = [
    path('result=<int:query_id>/', views.result, name='result')
]
