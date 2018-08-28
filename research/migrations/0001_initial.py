# Generated by Django 2.0.2 on 2018-03-06 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('title', models.CharField(max_length=200)),
                ('organization', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['-start', '-end'],
            },
        ),
    ]
