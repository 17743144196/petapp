# Generated by Django 2.1.1 on 2018-10-30 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_auto_20181030_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumcomment',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
