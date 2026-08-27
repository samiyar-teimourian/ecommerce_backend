from django.db import models

# Create your models here.
class product(models.Model):
    Product_ID= models.IntegerField()
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=172)
    price = models.IntegerField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to="products/")
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)
    is_available = models.BooleanField()
    def __str__(self):
        return str(self.id)