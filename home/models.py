from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.ImageField(upload_to='recipe_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class delivery(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    order = models.ForeignKey(Recipe,related_name="delivery_order", on_delete=models.CASCADE)
    
