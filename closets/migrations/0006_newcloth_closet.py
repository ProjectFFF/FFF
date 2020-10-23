# Generated by Django 3.1.1 on 2020-10-21 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('closets', '0005_auto_20201014_0539'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newcloth_closet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cloth_name_c', models.CharField(max_length=255)),
                ('shoulder_c', models.DecimalField(decimal_places=3, max_digits=6)),
                ('chest_c', models.DecimalField(decimal_places=3, max_digits=6)),
                ('arm_c', models.DecimalField(decimal_places=3, max_digits=6)),
                ('total_length_c', models.DecimalField(decimal_places=3, max_digits=6)),
                ('image_c', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('shopping_link_c', models.CharField(blank=True, max_length=255, null=True)),
                ('tag', models.CharField(blank=True, max_length=255, null=True)),
                ('review', models.CharField(blank=True, max_length=255, null=True)),
                ('pub_date', models.DateTimeField(blank=True, null=True, verbose_name='date published')),
            ],
        ),
    ]