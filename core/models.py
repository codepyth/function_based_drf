from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    quantity = models.DecimalField(max_digits=10, blank=False, null=False, decimal_places=2)

    def __str__(self) -> str:
        return self.name


class Property(models.Model):
    image1 = models.ImageField(upload_to='images/product_images')
    image2 = models.ImageField(upload_to='images/product_images')
    image3 = models.ImageField(upload_to='images/product_images')
    product_id = models.ForeignKey(
        Product, related_name='property', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.product_id.name + ' Properties'


class Financial(models.Model):
    salePrice = models.DecimalField(max_digits=10, decimal_places=2)
    costPrice = models.DecimalField(max_digits=10, decimal_places=2)
    product_id = models.ForeignKey(
        Product, related_name='financial', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.product_id.name


class Related(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.product_id.name


class Alternative(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.product_id.name


class ProductRelations(models.Model):
    product_id = models.ForeignKey(Product, related_name='product_relation', null=True, blank=True, on_delete=models.CASCADE)
    isRelated = models.ManyToManyField(Related)
    alternative = models.ManyToManyField(Alternative)
    
