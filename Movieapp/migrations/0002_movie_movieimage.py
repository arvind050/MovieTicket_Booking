# Generated by Django 3.0.4 on 2020-05-20 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='MovieImage',
            field=models.ImageField(default='No-image.jpg', upload_to='MovieImage/'),
        ),
    ]