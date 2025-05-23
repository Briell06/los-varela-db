"""Serializers for the main application."""

from rest_framework import serializers
from .models import Categoria, Item, Combo


class CategoriaSerializer(serializers.ModelSerializer):
    """
    Serializador para la categoría.
    """

    class Meta:
        """
        Meta para la categoría.
        """

        model = Categoria
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    """
    Serializador para el item.
    """

    categoria = serializers.StringRelatedField()

    class Meta:
        """
        Meta para el item.
        """

        model = Item
        fields = "__all__"


class ComboSerializer(serializers.ModelSerializer):
    """
    Serializador para el combo.
    """

    items = ItemSerializer(many=True)

    class Meta:
        """
        Meta para el combo.
        """

        model = Combo
        fields = "__all__"
