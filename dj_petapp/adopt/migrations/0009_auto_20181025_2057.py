# Generated by Django 2.1.1 on 2018-10-25 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopt', '0008_auto_20181023_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]
