# Generated by Django 3.0.5 on 2022-12-12 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0009_auto_20221212_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='.static/pizzas/media'),
        ),
    ]
