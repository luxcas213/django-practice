# Generated by Django 5.1.4 on 2024-12-26 16:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.project')),
            ],
        ),
    ]
