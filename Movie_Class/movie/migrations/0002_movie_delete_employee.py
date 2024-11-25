# Generated by Django 5.1.3 on 2024-11-24 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('language', models.CharField(max_length=20)),
                ('details', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
