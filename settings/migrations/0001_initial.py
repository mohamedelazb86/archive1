# Generated by Django 4.2 on 2025-01-22 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=75)),
                ('name', models.CharField(max_length=120)),
                ('notes', models.TextField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=75)),
                ('name', models.CharField(max_length=120)),
                ('notes', models.TextField(max_length=1500)),
            ],
        ),
    ]
