# Generated by Django 2.1 on 2018-08-10 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0002_auto_20180810_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='isbn',
            field=models.IntegerField(),
        ),
    ]
