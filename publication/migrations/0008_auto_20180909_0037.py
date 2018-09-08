# Generated by Django 2.1 on 2018-09-09 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0007_auto_20180821_2327'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-no']},
        ),
        migrations.AlterModelOptions(
            name='domestic',
            options={'ordering': ['-no']},
        ),
        migrations.AlterModelOptions(
            name='international',
            options={'ordering': ['-no']},
        ),
        migrations.RemoveField(
            model_name='book',
            name='NO',
        ),
        migrations.RemoveField(
            model_name='domestic',
            name='NO',
        ),
        migrations.RemoveField(
            model_name='international',
            name='NO',
        ),
        migrations.AddField(
            model_name='book',
            name='no',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='domestic',
            name='no',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='domestic',
            name='year',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='international',
            name='no',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='international',
            name='year',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
