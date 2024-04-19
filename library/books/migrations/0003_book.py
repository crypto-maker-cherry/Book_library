# Generated by Django 4.2.2 on 2023-07-08 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_students_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('total_copies', models.IntegerField()),
                ('available_copies', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='book_image')),
            ],
        ),
    ]