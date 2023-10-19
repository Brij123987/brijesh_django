from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE)
  image = models.ImageField(default='profilepic.jpeg', upload_to='profile_pictures')
  location = models.CharField(max_length=1000)
  user_type =  models.CharField(max_length=200, default='users')

  def __str__(self):
    return self.user.username

class CusOrders(models.Model):
  order_id = models.AutoField(primary_key=True)
  prod_code = models.IntegerField()
  quantity = models.IntegerField(default=1)
  user = models.CharField(max_length=200)

  def __str__(self):
    return str(
      (
        str(self.order_id),
        str(self.prod_code),
        str(self.quantity),
        str(self.user)
      )
    )
