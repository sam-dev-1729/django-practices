# Generated by Django 4.2.7 on 2023-12-04 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellers',
            name='banck_account',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
