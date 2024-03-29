# Generated by Django 5.0 on 2024-02-05 01:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_example'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, upload_to='upload')),
                ('title', models.CharField(blank=True, max_length=300)),
                ('status', models.IntegerField(blank=True, default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, upload_to='upload')),
            ],
        ),
        migrations.AddField(
            model_name='feedback',
            name='message',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.CreateModel(
            name='Tovar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo1', models.ImageField(blank=True, upload_to='upload')),
                ('logo2', models.ImageField(blank=True, upload_to='upload')),
                ('logo3', models.ImageField(blank=True, upload_to='upload')),
                ('logo4', models.ImageField(blank=True, upload_to='upload')),
                ('title', models.CharField(blank=True, max_length=300)),
                ('pokritiya_metalla', models.TextField(blank=True, max_length=500)),
                ('narujniy_panel', models.TextField(blank=True, max_length=500)),
                ('vnutnennit_panel', models.TextField(blank=True, max_length=500)),
                ('osnovnoy_zamok', models.TextField(blank=True, max_length=500)),
                ('dop_zamok', models.TextField(blank=True, max_length=500)),
                ('furnitura', models.TextField(blank=True, max_length=500)),
                ('dop_info', models.TextField(blank=True, max_length=500)),
                ('status', models.IntegerField(blank=True, default=0)),
                ('cat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
        ),
    ]
