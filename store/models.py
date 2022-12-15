from django.db import models

# Create your models here.
class Product(models.Model):
		name = models.CharField(max_length=64)
		price = models.FloatField(default=0.0)
		stock = models.IntegerField(default=0)
		description = models.TextField(blank=True)
		image = models.ImageField(upload_to='products')

		def __str__(self):
				return self.name