# Generated by Django 4.1.7 on 2023-06-26 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servive', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventname', models.CharField(max_length=122)),
                ('eventid', models.CharField(max_length=12)),
            ],
        ),
    ]
