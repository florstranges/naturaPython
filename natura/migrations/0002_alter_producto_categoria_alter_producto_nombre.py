# Generated by Django 4.1.7 on 2023-03-31 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('natura', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
