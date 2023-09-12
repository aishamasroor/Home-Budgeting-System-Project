from django.db import models


# Create your models here.
class Category(models.Model):
    objects = None
    cat_id = models.CharField(max_length=20, primary_key=True)
    cat_names = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.cat_names



class Transaction(models.Model):
    objects = None
    expense = models.CharField(max_length=100)
    amount = models.IntegerField(default=0)
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
