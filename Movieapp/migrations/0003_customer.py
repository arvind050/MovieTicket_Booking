# Generated by Django 3.0.4 on 2020-06-09 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movieapp', '0002_movie_movieimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('custId', models.AutoField(primary_key=True, serialize=False)),
                ('custName', models.CharField(max_length=50)),
                ('custLname', models.CharField(max_length=50)),
                ('custEmail', models.CharField(max_length=50, unique=True)),
                ('custPassword', models.CharField(max_length=50)),
                ('custContact', models.CharField(max_length=12)),
                ('custAddress', models.CharField(max_length=225)),
            ],
            options={
                'db_table': 'customer_005',
            },
        ),
    ]
