from django.urls import path
from .views import MarketFieldsView, QueryView
from django.urls import path, include
urlpatterns = [

    # List and Create
    path('market-fields/', MarketFieldsView.as_view(), name='market-fields-list'),  # For GET and POST
    # Detail, Update, and Delete by pk
    path('market-fields/<int:pk>/', MarketFieldsView.as_view(), name='market-fields-detail'),  # For PUT and DELETE

    path('query/', QueryView.as_view(), name='query'),  # For Query market fields
]
