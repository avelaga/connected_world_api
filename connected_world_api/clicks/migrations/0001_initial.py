# Generated by Django 3.2 on 2021-04-22 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=200, null=True)),
                ('time', models.CharField(max_length=200, null=True)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('hue', models.IntegerField()),
            ],
        ),
    ]