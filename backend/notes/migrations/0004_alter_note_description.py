# Generated by Django 3.2.4 on 2021-06-22 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_alter_note_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]