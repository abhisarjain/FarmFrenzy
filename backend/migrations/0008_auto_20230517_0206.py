# Generated by Django 3.2 on 2023-05-16 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_negotiation_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='negotiation',
            name='status',
        ),
        migrations.AddField(
            model_name='negotiation',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='negotiation',
            name='awaited',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='negotiation',
            name='rejected',
            field=models.BooleanField(default=False),
        ),
    ]
