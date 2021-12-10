from django.db import models
from django.utils import timezone
#from PIL import Image

class Product(models.Model):
  code = models.CharField(max_length=200,default="000-0000")
  name = models.CharField(max_length=200,default="Unnamed")
  description = models.CharField(max_length=200,default="N/A")
  price = models.DecimalField(max_digits=10,decimal_places=2,default="0.00")
  date_entry = models.DateTimeField(default=timezone.now())
#  photo = models.ImageField(upload_to='images/')

  def __str__(self):
    return self.name
