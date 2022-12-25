# Generated by Django 4.1.4 on 2022-12-25 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('products_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('price', models.IntegerField()),
                ('image_url', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.categories')),
            ],
            options={
                'db_table': 'shop_products',
            },
        ),
    ]
