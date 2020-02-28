# Generated by Django 2.2 on 2020-02-28 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0011_auto_20200228_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cart.TransactionMethod'),
            preserve_default=False,
        ),
    ]
