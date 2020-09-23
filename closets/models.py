from django.db import models

# Create your models here.

class Newcloth(models.Model):
    cloth_name = models.CharField(max_length=255)
    shoulder = models.DecimalField(max_digits=6, decimal_places=3)
    chest = models.DecimalField(max_digits=6, decimal_places=3)
    arm = models.DecimalField(max_digits=6, decimal_places=3)
    total_length = models.DecimalField(max_digits=6, decimal_places=3)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.cloth_name