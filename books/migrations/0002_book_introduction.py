# Generated by Django 2.1.4 on 2018-12-12 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='introduction',
            field=models.TextField(default='Default Introduction'),
            preserve_default=False,
        ),
    ]
