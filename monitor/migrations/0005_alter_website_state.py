# Generated by Django 3.2.16 on 2023-01-12 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0004_alter_website_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='state',
            field=models.CharField(default='active', max_length=8),
        ),
    ]
