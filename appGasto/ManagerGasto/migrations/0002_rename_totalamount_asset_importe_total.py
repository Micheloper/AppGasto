# Generated by Django 4.0.4 on 2022-05-04 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManagerGasto', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asset',
            old_name='totalamount',
            new_name='importe_Total',
        ),
    ]