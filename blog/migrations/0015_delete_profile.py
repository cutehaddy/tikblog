# Generated by Django 3.2.6 on 2021-08-12 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]