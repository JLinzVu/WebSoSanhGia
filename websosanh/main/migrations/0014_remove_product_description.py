# Generated by Django 3.2.7 on 2021-12-04 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_product_vector_column'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
    ]
