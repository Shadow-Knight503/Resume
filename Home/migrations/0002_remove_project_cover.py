# Generated by Django 4.1.3 on 2024-02-15 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='Cover',
        ),
    ]