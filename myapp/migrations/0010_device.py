# Generated by Django 4.1.9 on 2023-06-20 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_categories_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('img', models.CharField(max_length=300)),
                ('desc', models.TextField(max_length=500)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
