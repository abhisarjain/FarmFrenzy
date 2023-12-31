# Generated by Django 3.2 on 2023-05-16 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_delete_negotiation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Negotiation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proposed_price', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=100)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.buyer')),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.crop')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.seller')),
            ],
        ),
    ]
