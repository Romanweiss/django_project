# Generated by Django 5.0.3 on 2024-03-18 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appResponseData', '0002_alter_generatetab_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generatetab',
            name='number',
            field=models.PositiveIntegerField(default=507, verbose_name='Число'),
        ),
    ]
