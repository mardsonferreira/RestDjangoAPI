# Generated by Django 2.2 on 2019-04-10 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190410_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='version',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
