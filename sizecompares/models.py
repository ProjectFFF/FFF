from django.db import models

# Create your models here.
class Compare(models.Model):
    shoulder_compare = models.DecimalField(max_digits=6, decimal_places=3)
    chest_compare = models.DecimalField(max_digits=6, decimal_places=3)
    arm_compare = models.DecimalField(max_digits=6, decimal_places=3)
    total_length_compare = models.DecimalField(max_digits=6, decimal_places=3)