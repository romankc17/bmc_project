# Generated by Django 3.2.4 on 2021-06-18 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(default='media/events/event_default.jpg', upload_to='events/'),
        ),
    ]