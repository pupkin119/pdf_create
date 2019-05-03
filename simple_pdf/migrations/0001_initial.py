# Generated by Django 2.1.1 on 2019-01-20 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('upload', models.FileField(blank=True, null=True, upload_to='design/')),
            ],
        ),
        migrations.CreateModel(
            name='Fonts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('upload', models.FileField(blank=True, null=True, upload_to='fonts/')),
            ],
        ),
    ]
