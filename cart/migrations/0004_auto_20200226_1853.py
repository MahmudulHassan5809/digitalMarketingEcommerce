# Generated by Django 2.2 on 2020-02-26 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_order_product_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='bill',
            new_name='total_bill',
        ),
        migrations.AddField(
            model_name='order',
            name='product_price',
            field=models.CharField(default='XXXXXXXXXXXXXXXXXXXX', max_length=255),
            preserve_default=False,
        ),
    ]
