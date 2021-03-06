# Generated by Django 2.0.2 on 2018-03-05 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AP2047',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=200)),
                ('handout', models.FileField(blank=True, null=True, upload_to='AP2047/')),
                ('handout_type', models.CharField(choices=[('LC', 'Lecture'), ('AP', 'Appendix')], default='LC', max_length=2)),
            ],
        ),
    ]
