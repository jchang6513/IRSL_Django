# Generated by Django 2.0.2 on 2018-02-16 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('content', models.TextField(blank=True)),
                ('more', models.URLField(blank=True)),
            ],
        ),
    ]
