# Generated by Django 5.0 on 2024-01-25 07:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intel_app', '0012_agentisharebundleprice_agentmtnbundleprice_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='admininfo',
            name='momo_number',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='admininfo',
            name='payment_channel',
            field=models.CharField(choices=[('MTN Mobile Money', 'MTN Mobile Money'), ('Vodafone Cash', 'Vodafone Cash'), ('AT Money', 'AT Money')], default='MTN Mobile Money', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topuprequest',
            name='credited_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topuprequest',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mtntransaction',
            name='transaction_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Failed', 'Failed')], default='Completed', max_length=100),
        ),
    ]
