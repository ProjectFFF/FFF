from django.db import models

class Guide(models.Model):
    guide_name = models.CharField(max_length=255)
    guide_image = models.ImageField(upload_to='images/')
   

    def __str__(self):
        return self.guide_name
