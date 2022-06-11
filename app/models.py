from django.db import models

# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self) -> str:
        return f"{self.name}"


    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField("nom produit",max_length=100)
    desc = models.TextField()
    price=models.FloatField(default=0)
    created_at= models.DateField(auto_now_add=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self) -> str:
        return f"{self.name}"
