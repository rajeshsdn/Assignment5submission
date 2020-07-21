# Generated by Django 3.0.7 on 2020-07-20 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WFreq',
            fields=[
                ('wordid', models.AutoField(primary_key=True, serialize=False)),
                ('ttextmanageid', models.CharField(max_length=45)),
                ('word', models.CharField(max_length=45)),
                ('frequency', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'wview',
            },
        ),
    ]