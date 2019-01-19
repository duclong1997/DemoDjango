# Generated by Django 2.1.4 on 2018-12-16 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('numberPost', models.IntegerField(default=0)),
                ('datetime', models.DateField(auto_now_add=True)),
                ('body', models.TextField()),
            ],
        ),
    ]