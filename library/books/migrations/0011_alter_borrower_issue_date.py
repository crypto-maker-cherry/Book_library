# Generated by Django 4.2.2 on 2023-07-09 14:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_remove_book_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='issue_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 9, 14, 13, 12, 26709, tzinfo=datetime.timezone.utc)),
        ),
    ]
