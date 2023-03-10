# Generated by Django 4.1.4 on 2022-12-25 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('cinema_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('image_url', models.TextField()),
                ('address', models.TextField()),
                ('detail_address', models.TextField()),
            ],
            options={
                'db_table': 'movies_cinema',
            },
        ),
    ]
