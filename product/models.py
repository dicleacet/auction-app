from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(default='This is cool!')
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title