# Generated by Django 4.2.2 on 2023-07-07 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
