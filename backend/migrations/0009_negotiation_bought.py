# Generated by Django 3.2 on 2023-05-16 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_auto_20230517_0206'),
    ]

    operations = [
        migrations.AddField(
            model_name='negotiation',
            name='bought',
            field=models.BooleanField(default=False),
        ),
    ]
