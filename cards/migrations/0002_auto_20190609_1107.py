# Generated by Django 2.2.2 on 2019-06-09 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='img_url',
        ),
        migrations.RemoveField(
            model_name='card',
            name='value',
        ),
        migrations.AlterField(
            model_name='card',
            name='rank',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='card',
            name='suit',
            field=models.IntegerField(default=1),
        ),
    ]
