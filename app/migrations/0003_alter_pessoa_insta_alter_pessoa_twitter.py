# Generated by Django 4.2.5 on 2023-09-26 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_pais_continente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='insta',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='twitter',
            field=models.CharField(max_length=50),
        ),
    ]
