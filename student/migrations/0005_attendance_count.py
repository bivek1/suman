# Generated by Django 3.1.5 on 2021-02-08 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20210126_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]