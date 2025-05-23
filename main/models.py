from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.nombre}"


class Item(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to="items/", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name="items"
    )

    def __str__(self) -> str:
        return f"{self.nombre}"


class Combo(models.Model):

    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    items = models.ManyToManyField(Item, related_name="items_combo")
    imagen = models.ImageField(upload_to="combos/", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.nombre}"
