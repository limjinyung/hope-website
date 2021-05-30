# Generated by Django 3.1.6 on 2021-03-15 16:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hope_app', '0010_auto_20210312_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=1),
        ),
        migrations.AlterField(
            model_name='posttag',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 15, 16, 29, 2, 771111, tzinfo=utc)),
        ),
    ]