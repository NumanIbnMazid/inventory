from django.urls import path
from .views import ProductCreateView, ProductListView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('add/', ProductCreateView.as_view(), name='add_product'),
    path('list/', ProductListView.as_view(), name='list_product'),
    path('<slug>/update/', ProductUpdateView.as_view(), name='update_product'),
    path('<slug>/delete/', ProductDeleteView.as_view(), name='delete_product'),
]
