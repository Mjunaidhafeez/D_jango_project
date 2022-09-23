from django.db import models

class Category(models.Model):
    category_name= models.CharField(max_length=30)
    category_description=models.CharField(max_length=20,default='')

    def __str__(self):
        return self.category_name
