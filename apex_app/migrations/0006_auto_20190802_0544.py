# Generated by Django 2.2.2 on 2019-08-02 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apex_app', '0005_auto_20190802_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='user_id',
            field=models.BigIntegerField(default=0),
        ),
    ]
