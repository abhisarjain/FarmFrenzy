# Generated by Django 3.2 on 2023-05-16 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_negotiation'),
    ]

    operations = [
        migrations.AddField(
            model_name='negotiation',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
