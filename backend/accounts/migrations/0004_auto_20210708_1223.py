# Generated by Django 3.2.4 on 2021-07-08 06:38

import accounts.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_userprofile_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='address',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='accounts/default.png', upload_to=accounts.models.get_img_upload_path),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='permanent_address',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='sec',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B')], default='A', max_length=1),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='temporary_address',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
