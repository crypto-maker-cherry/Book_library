# Generated by Django 4.2.2 on 2023-07-08 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_available_copies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='available_copies',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
