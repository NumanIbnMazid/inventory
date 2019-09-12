from django.urls import path
from .views import ProductListView, ProductDetailView, UserListView, UserDetailView

urlpatterns = [
    path('product/list/', ProductListView.as_view()),
    path('product/<pk>/', ProductDetailView.as_view()),
    path('user/list/', UserListView.as_view()),
    path('user/<pk>/', UserDetailView.as_view()),
]
