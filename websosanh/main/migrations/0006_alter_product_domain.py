# Generated by Django 3.2.7 on 2021-11-07 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_product_domain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='domain',
            field=models.CharField(default='sendo.vn', max_length=40, null=True),
        ),
    ]
