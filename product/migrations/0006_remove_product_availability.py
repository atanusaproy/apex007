# Generated by Django 2.2.2 on 2019-12-01 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20191201_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='availability',
        ),
    ]
