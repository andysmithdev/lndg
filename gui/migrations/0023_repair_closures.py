# Generated by Django 3.2.7 on 2022-03-11 23:31

from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0022_auto_20220227_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='channels',
            name='fees_updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='channels',
            name='auto_fees',
            field=models.BooleanField(default=False),
        ),
    ]