# Generated by Django 4.2.7 on 2023-12-22 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addcategory',
            name='task',
        ),
    ]
