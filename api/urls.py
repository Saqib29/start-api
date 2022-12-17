from django.urls import path
from .views import ItemList, ItemDetails, LocationList, LocationDetail

urlpatterns = [
    path('item/', ItemList.as_view()),
    path('item/<int:pk>/', ItemDetails.as_view()),
    path('location/', LocationList.as_view()),
    path('location/<int:pk>/', LocationDetail.as_view()),
]