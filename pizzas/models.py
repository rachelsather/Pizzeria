from django.db import models

# Create your models here.

class Pizza(models.Model):
    pizza_name = models.CharField(max_length=200)
    pizza_image = models.ImageField(upload_to='images/',blank=True,null=True)

    def __str__(self):
        return self.pizza_name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.TextField()

    def __str__(self):
        return f"{self.topping_name[:20]}"

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    comment_name = models.TextField()
    #date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Image(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='.static/pizzas/media')

    def __str__(self):
        return self.title