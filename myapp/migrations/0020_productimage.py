# Generated by Django 3.2.5 on 2021-09-09 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_alter_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='productimg')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
            ],
        ),
    ]
