# Generated by Django 2.2.2 on 2019-12-01 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20191201_1543'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='active',
            new_name='status',
        ),
    ]
