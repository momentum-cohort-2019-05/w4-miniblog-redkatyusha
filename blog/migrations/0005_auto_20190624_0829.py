# Generated by Django 2.2.2 on 2019-06-24 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190621_0354'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-date_posted', 'blogger']},
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='pubdate',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
