# Generated by Django 5.0.7 on 2024-08-15 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_usercourse_payment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
