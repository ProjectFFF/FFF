# Generated by Django 3.1.1 on 2020-10-24 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('closets', '0007_auto_20201023_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='newcloth',
            name='writer',
            field=models.CharField(default='admin', max_length=255),
        ),
    ]
