# Generated by Django 3.0.3 on 2020-06-26 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0002_auto_popuate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passenger',
            name='rate',
        ),
    ]
