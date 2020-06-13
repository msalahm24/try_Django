from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.FloatField()
    stock=models.IntegerField()
    image_url=models.CharField(max_length=2083)
    discription=models.CharField(max_length=500,default='leather bag')
    # def __str__(self):
    #     self.name


class Offer(models.Model):
    code=models.CharField(max_length=100)
    description=models.TextField(blank=True,null=True)
    discount=models.FloatField()
