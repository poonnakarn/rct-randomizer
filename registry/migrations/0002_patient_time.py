# Generated by Django 3.2.9 on 2021-11-16 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
    ]