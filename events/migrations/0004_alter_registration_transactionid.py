# Generated by Django 4.2 on 2025-02-15 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_registration_transactionid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='transactionid',
            field=models.CharField(max_length=100),
        ),
    ]
