# Generated by Django 2.2.2 on 2019-06-08 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suit', models.CharField(max_length=1)),
                ('rank', models.CharField(max_length=1)),
                ('value', models.IntegerField(default=0)),
                ('img_url', models.CharField(max_length=200)),
            ],
        ),
    ]
