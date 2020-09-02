from django.urls import path

from . import views

urlpatterns = [
    path('queryId=<int:query_id>/', views.result, name='query_id'),
    path('index/queryId=<int:query_id>/', views.index, name='query_id')

]
