# Generated by Django 2.2.2 on 2019-06-21 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='bodytext',
            field=models.TextField(default='fillertext', max_length=100000),
            preserve_default=False,
        ),
    ]
