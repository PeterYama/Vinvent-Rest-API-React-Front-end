# Generated by Django 3.1 on 2020-08-20 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='body',
            field=models.TextField(default='Must be Done !'),
            preserve_default=False,
        ),
    ]
