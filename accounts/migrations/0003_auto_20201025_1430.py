# Generated by Django 3.1.1 on 2020-10-25 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201024_0141'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='height',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='member',
            name='weight',
            field=models.IntegerField(default=0),
        ),
    ]
