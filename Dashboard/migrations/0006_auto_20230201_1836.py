# Generated by Django 2.2.12 on 2023-02-01 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0005_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='no_hp',
            field=models.IntegerField(),
        ),
    ]
