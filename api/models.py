from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True, unique=True)
    discription = models.TextField(max_length=100, null = True, blank= True, unique=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    discription = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    

    #this is test change to push to github