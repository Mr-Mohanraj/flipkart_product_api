# Generated by Django 4.1.7 on 2023-04-17 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productApi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiuser',
            name='api_token_password',
            field=models.TextField(blank=True, max_length=10, null=True),
        ),
    ]