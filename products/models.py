from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()
    price = models.FloatField()
    rate = models.DecimalField(max_digits=10, decimal_places=1)


    def __str__(self):
        return self.title



class Review(models.Model):
    text = models.TextField(max_length=350)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.text
