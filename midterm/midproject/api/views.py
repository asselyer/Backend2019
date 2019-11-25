from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, mixins, permissions
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from api.serializers import UserSerializer, ProductSerializer, ServiceSerializer
from api.models import MainUser, Product, Service

class RegisterUser(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return MainUser.objects.all()
        

# class ProductListViewSet(mixins.RetrieveModelMixin,
#                          mixins.ListModelMixin,
#                          viewsets.GenericViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductListSerializer


# class ServiceDetailViewSet(mixins.RetrieveModelMixin,
#                            mixins.UpdateModelMixin,
#                            mixins.DestroyModelMixin,
#                            viewsets.GenericViewSet):
#     queryset = Service.objects.all()
#     serializer_class = ServiceListSerializer


class ProductViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated,)

    serializer_class = ProductSerializer


class ServiceViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = Service.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ServiceSerializer
        if self.action != 'retrieve':
            return ServiceSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get']

class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    http_method_names = ['get']


