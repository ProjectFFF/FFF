# Generated by Django 3.1.1 on 2020-10-23 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('closets', '0006_newcloth_closet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newcloth_closet',
            old_name='shopping_link_c',
            new_name='shopping_link',
        ),
    ]
