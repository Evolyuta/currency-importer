# Generated by Django 3.2.7 on 2021-09-01 17:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0002_auto_20210901_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='code',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
