# Generated by Django 2.2.2 on 2019-07-22 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apex_app', '0003_auto_20190722_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
    ]
