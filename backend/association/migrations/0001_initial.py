# Generated by Django 3.2.4 on 2021-06-17 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=2000)),
                ('venue', models.CharField(max_length=50)),
                ('host', models.CharField(max_length=50, null=True)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
