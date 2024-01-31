# Generated by Django 5.0 on 2024-01-31 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appKey', '0003_product_currency_alter_product_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('RU', 'Рубль'), ('US', 'Доллар'), ('CHINA', 'Юань'), ('EU', 'Евро')], default='RU', max_length=10, verbose_name='Валюта'),
        ),
    ]