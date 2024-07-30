# Generated by Django 5.0.7 on 2024-07-30 12:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchPrompt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_prompt', models.CharField(max_length=100, verbose_name='search prompt')),
            ],
        ),
        migrations.CreateModel(
            name='GeneratedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(verbose_name='image url')),
                ('search', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aigeneration.searchprompt')),
            ],
        ),
    ]
