# Generated by Django 3.2.4 on 2021-06-22 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_alter_note_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='file',
            field=models.FileField(upload_to='notes/%Y/%m/%d/'),
        ),
    ]