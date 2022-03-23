# Generated by Django 3.2.7 on 2022-03-11 23:31

from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0024_autofees'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Resolutions',
        ),
        migrations.DeleteModel(
            name='Closures',
        ),
        migrations.CreateModel(
            name='Closures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chan_id', models.CharField(max_length=20)),
                ('funding_txid', models.CharField(max_length=64)),
                ('funding_index', models.IntegerField()),
                ('closing_tx', models.CharField(max_length=64)),
                ('remote_pubkey', models.CharField(max_length=66)),
                ('capacity', models.BigIntegerField()),
                ('close_height', models.IntegerField()),
                ('settled_balance', models.BigIntegerField()),
                ('time_locked_balance', models.BigIntegerField()),
                ('close_type', models.IntegerField()),
                ('open_initiator', models.IntegerField()),
                ('close_initiator', models.IntegerField()),
                ('resolution_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Resolutions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resolution_type', models.IntegerField()),
                ('outcome', models.IntegerField()),
                ('outpoint_tx', models.CharField(max_length=64)),
                ('outpoint_index', models.IntegerField()),
                ('amount_sat', models.BigIntegerField()),
                ('sweep_txid', models.CharField(max_length=64)),
                ('chan_id', models.CharField(max_length=20)),
            ],
        ),
    ]