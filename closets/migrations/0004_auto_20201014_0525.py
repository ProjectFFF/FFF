# Generated by Django 3.1.1 on 2020-10-13 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('closets', '0003_auto_20201011_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newcloth',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.CreateModel(
            name='Photocloset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addimage', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('newcloth', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='closets.newcloth')),
            ],
        ),
    ]