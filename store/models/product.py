from django.db import models
from .category import Category
class Product(models.Model):
    product_name= models.CharField(max_length=30)
    product_catgory=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    product_price=models.IntegerField(default=0)
    product_description=models.CharField(max_length=200,default='',null=True,blank=True)
    product_image=models.ImageField(upload_to='uploads/products')
    @staticmethod
    def get_all_products():
        return Product.objects.all()


