# Generated by Django 5.0.6 on 2024-05-26 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_contact_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='desc',
        ),
    ]