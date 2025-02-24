# Generated by Django 4.2 on 2025-02-13 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.EmailField(default='abc@gmail.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='registration',
            name='event',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='registration',
            name='image',
            field=models.ImageField(upload_to='registration_images/'),
        ),
    ]
