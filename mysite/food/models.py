from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
  user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        default= '1'
  )
  prod_code = models.IntegerField(default=100)
  for_user = models.CharField(max_length=100, 
                              default='xyz'
                              )
  item_name = models.CharField(max_length=50)
  item_desc = models.CharField(
    max_length=500,
    default='Lorem ipsum dolor, sit amet consectetur adipisicing elit. Eveniet, et iste earum error consequuntur aspernatur aperiam similique natus voluptate repellat assumenda sapiente. Deleniti, natus molestias. Necessitatibus provident quis officiis dolor.'
    )
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
  
