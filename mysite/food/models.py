from django.db import models

# Create your models here.

class Item(models.Model):
  item_name = models.CharField(max_length=50)
  item_desc = models.CharField(max_length=300)
  items_price = models.IntegerField()
  item_image = models.CharField(max_length=500, default="https://livingstonbagel.com/wp-content/uploads/2016/11/food-placeholder.jpg")

  # def __str__(self):
  #   return str((
  #     str(self.item_name),
  #     str(self.item_desc),
  #     str(self.items_price)
  #   ))
  def __str__(self):
    return self.item_name
  
