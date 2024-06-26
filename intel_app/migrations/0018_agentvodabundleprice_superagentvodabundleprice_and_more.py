# Generated by Django 5.0 on 2024-06-07 14:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intel_app', '0017_announcement'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentVodaBundlePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('bundle_volume', models.FloatField()),
                ('purchase_price', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SuperAgentVodaBundlePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('bundle_volume', models.FloatField()),
                ('purchase_price', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VodaBundlePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('bundle_volume', models.FloatField()),
                ('purchase_price', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VodafoneTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bundle_number', models.BigIntegerField()),
                ('offer', models.CharField(max_length=250)),
                ('reference', models.CharField(blank=True, max_length=20)),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('transaction_status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Processing', 'Processing'), ('Failed', 'Failed')], default='Pending', max_length=100)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
