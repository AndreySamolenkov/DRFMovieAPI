# Generated by Django 4.1.1 on 2023-01-28 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='images/none/sampleimg.jpg', upload_to='images'),
        ),
    ]
