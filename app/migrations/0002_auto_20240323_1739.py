# Generated by Django 3.2.8 on 2024-03-23 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salarios',
            name='extra_dic',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='salarios',
            name='extra_jun',
            field=models.BooleanField(default=False),
        ),
    ]
