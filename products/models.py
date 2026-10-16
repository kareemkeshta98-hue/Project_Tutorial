from django.db import models
from datetime import datetime

# Create your models here.
class product(models.Model):
    x = [
         ('Phone' , 'Phone'),
         ('PC' , 'PC'),
    ]
    name = models.CharField(max_length=50,default='Product Name',verbose_name='Title')
    content = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    image = models.ImageField(upload_to='photos/%y/%m/%d',default='photos/26/9/6/jpg')
    active = models.BooleanField(default=True)
    Category = models.CharField(max_length=50,null=True,blank=True,choices=x)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'PRODUCT'

    class Meta:
            ordering = ['name']

class Test (models.Model):
     date = models.DateField()
     time = models.TimeField(null=True)
     created = models.DateTimeField(default=datetime.now)
     

