from rest_framework.generics import ListAPIView, RetrieveAPIView
from products.models import Product
from django.contrib.auth.models import User
from .serializers import ProductSerializer, UserSerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(RetrieveAPIView):
    # lookup_field = "pk"
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    # lookup_field = "pk"
    queryset = User.objects.all()
    serializer_class = UserSerializer
