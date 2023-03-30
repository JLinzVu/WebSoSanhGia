# Generated by Django 3.2.7 on 2021-11-07 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_product_domain'),
    ]

    operations = [
        migrations.AddField(
            model_name='web_information',
            name='logo',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='web_information',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
