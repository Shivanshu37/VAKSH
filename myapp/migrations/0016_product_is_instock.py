# Generated by Django 3.2.5 on 2021-09-06 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_product_prod_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_inStock',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]