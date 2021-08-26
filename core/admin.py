from django.contrib import admin
from .models import Alternative, Product, Financial, Property, ProductRelations, Related
# Register your models here.

admin.site.register(Product)
admin.site.register(Property)
admin.site.register(Financial)
admin.site.register(Related)
admin.site.register(Alternative)
admin.site.register(ProductRelations)