# Generated by Django 3.2.18 on 2023-03-20 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(default='Unknown', max_length=20),
        ),
    ]