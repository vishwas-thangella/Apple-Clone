# Generated by Django 4.1.9 on 2023-06-20 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_device'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='model',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
