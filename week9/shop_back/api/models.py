from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=300)

    def to_json(self):
        return {
            'id':self.id,
            'name': self.name,
        }


class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField(default=1000)
    description = models.TextField(default='description')
    count = models.IntegerField(default=5)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def to_json(self):
        return {
            'id':self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'category': self.category_id,
        }