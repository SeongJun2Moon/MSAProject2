# Generated by Django 4.1.4 on 2022-12-25 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
        ('busers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('comments_id', models.IntegerField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updatated_at', models.DateTimeField(auto_now=True)),
                ('parent_id', models.TextField(null=True)),
                ('blog_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='busers.busers')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.posts')),
            ],
            options={
                'db_table': 'blog_comments',
            },
        ),
    ]
