# Generated by Django 3.0.5 on 2022-12-12 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0007_auto_20221212_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='./media/images/'),
        ),
    ]
