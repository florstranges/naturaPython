# Generated by Django 4.1.7 on 2023-04-17 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('natura', '0006_mensaje_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Consultora',
        ),
    ]