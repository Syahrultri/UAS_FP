# Generated by Django 2.2.12 on 2023-02-01 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0004_auto_20221101_1012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('no_hp', models.IntegerField(max_length=15)),
                ('provinsi', models.CharField(max_length=20)),
                ('kota', models.CharField(max_length=20)),
                ('kode_pos', models.IntegerField()),
                ('waktu_posting', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
