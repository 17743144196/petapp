# Generated by Django 2.1.1 on 2018-10-22 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('picture', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=4000)),
                ('like', models.IntegerField(null=True)),
                ('lookers', models.IntegerField(null=True)),
                ('contact', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('weixin', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=50, null=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.type')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
