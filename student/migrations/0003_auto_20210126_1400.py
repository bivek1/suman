# Generated by Django 3.1.5 on 2021-01-26 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_attendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='evening',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='morning',
            field=models.TimeField(),
        ),
    ]