# Generated by Django 2.0.2 on 2018-03-05 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_auto_20180305_2236'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classname',
            options={'ordering': ['-date']},
        ),
    ]
