# Generated by Django 5.0 on 2023-12-30 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='users',
        ),
    ]
