from django.db import models

# Create your models here.


# User Model
class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    user_email = models.EmailField(max_length=200, unique=True)
    user_password = models.CharField(max_length=50)
    user_image = models.ImageField(default="/images/HCU_LOGO.jpg")
