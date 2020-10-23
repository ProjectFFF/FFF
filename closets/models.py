from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Newcloth(models.Model):
    cloth_name = models.CharField(max_length=255)
    shoulder = models.DecimalField(max_digits=6, decimal_places=3)
    chest = models.DecimalField(max_digits=6, decimal_places=3)
    arm = models.DecimalField(max_digits=6, decimal_places=3)
    total_length = models.DecimalField(max_digits=6, decimal_places=3)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    shopping_link = models.CharField(max_length=255, blank=True, null=True)
    tag = models.CharField(max_length=255, blank=True, null=True)
    review = models.CharField(max_length=255, blank=True, null=True)
    pub_date = models.DateTimeField('date published', blank=True, null=True)

    def __str__(self):
        return self.cloth_name

class Newcloth_closet(models.Model):
    cloth_name_c = models.CharField(max_length=255)
    shoulder_c = models.DecimalField(max_digits=6, decimal_places=3)
    chest_c = models.DecimalField(max_digits=6, decimal_places=3)
    arm_c = models.DecimalField(max_digits=6, decimal_places=3)
    total_length_c = models.DecimalField(max_digits=6, decimal_places=3)
    image_c = models.ImageField(upload_to='images/', blank=True, null=True)
    shopping_link = models.CharField(max_length=255, blank=True, null=True)
    tag = models.CharField(max_length=255, blank=True, null=True)
    review = models.CharField(max_length=255, blank=True, null=True)
    pub_date = models.DateTimeField('date published', blank=True, null=True)

    def __str__(self):
        return self.cloth_name_c

# class Photocloset(models.Model):
    # newcloth = models.ForeignKey(Newcloth, on_delete=models.CASCADE, null=True)
    # addimage = models.ImageField(upload_to='images/', blank=True, null=True)