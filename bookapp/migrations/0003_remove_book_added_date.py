# Generated by Django 5.0.3 on 2024-03-16 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0002_remove_book_file_alter_book_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='added_date',
        ),
    ]
