# Generated by Django 2.1.1 on 2018-10-23 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopt', '0007_auto_20181023_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
