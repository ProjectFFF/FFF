from django.db import models


class Member(models.Model):
    id_m = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_naumber = models.CharField(max_length=255)
    height = models.IntegerField(default=0)
    weight =models.IntegerField(default=0) 

    def __str__(self):
        return self.id_m
