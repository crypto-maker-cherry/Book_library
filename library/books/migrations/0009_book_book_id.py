# Generated by Django 4.2.2 on 2023-07-09 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_alter_students_rollno'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_id',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
    ]
