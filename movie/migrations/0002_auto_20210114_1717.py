# Generated by Django 3.1.5 on 2021-01-14 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='stars',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=2),
        ),
    ]