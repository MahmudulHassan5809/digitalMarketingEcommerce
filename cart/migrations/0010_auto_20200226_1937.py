# Generated by Django 2.2 on 2020-02-26 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_auto_20200226_1935'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='seller',
            new_name='sellers',
        ),
    ]
