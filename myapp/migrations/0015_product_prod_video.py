# Generated by Django 3.2.5 on 2021-09-06 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_alter_orderplaced_discounted'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prod_video',
            field=models.CharField(blank=True, max_length=10000),
        ),
    ]
