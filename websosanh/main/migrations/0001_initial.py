# Generated by Django 3.2.7 on 2021-11-06 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='my_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(max_length=1000)),
                ('name', models.CharField(max_length=300, null=True)),
                ('price', models.CharField(max_length=20, null=True)),
                ('image_link', models.TextField(max_length=1000)),
                ('description', models.TextField(default='', max_length=1000, null=True)),
                ('brand', models.CharField(default='', max_length=30, null=True)),
                ('category', models.TextField(default='', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='web_information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.TextField(default='', max_length=40)),
                ('url', models.TextField(default='', max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='product_xpath',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_xpath', models.CharField(max_length=50)),
                ('url_xpath', models.CharField(max_length=50)),
                ('name_xpath', models.CharField(max_length=50)),
                ('price_xpath', models.CharField(max_length=50)),
                ('image_xpath', models.CharField(max_length=100)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.web_information')),
            ],
        ),
        migrations.CreateModel(
            name='my_subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('parent_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.my_category')),
            ],
        ),
    ]
