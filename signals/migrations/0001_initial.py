# Generated by Django 3.2.9 on 2021-11-17 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LOG_IN_SIGNALS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=50)),
                ('request_path', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='LOG_OUT_SIGNALS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=50)),
                ('request_path', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
