# Generated by Django 3.2.5 on 2021-08-29 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_orderplaced_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderplaced',
            name='discounted',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
