# Generated by Django 2.0.2 on 2018-03-06 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0005_auto_20180306_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='location',
            field=models.CharField(max_length=200),
        ),
    ]
