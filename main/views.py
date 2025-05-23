from django.shortcuts import render
from rest_framework import viewsets
from .models import Categoria, Item, Combo
from .serializer import CategoriaSerializer, ItemSerializer, ComboSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    """
    Vista para la categoría.
    """

    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ItemViewSet(viewsets.ModelViewSet):
    """
    Vista para el item.
    """

    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ComboViewSet(viewsets.ModelViewSet):
    """
    Vista para el combo.
    """

    queryset = Combo.objects.all()
    serializer_class = ComboSerializer
