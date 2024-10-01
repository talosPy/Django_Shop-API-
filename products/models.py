from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=255, null=True)
    popularity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.popularity}"



class Product(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    category = models.ManyToManyField(Category,related_name="products")
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')  # Add this line

    
    def __str__(self):
        return f"{self.name} - {self.price}"
