# Generated by Django 4.0 on 2022-01-10 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_watch'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='isclosed',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]