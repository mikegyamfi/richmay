# Generated by Django 5.0 on 2024-09-17 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intel_app', '0018_agentvodabundleprice_superagentvodabundleprice_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='admininfo',
            name='ishare_source',
            field=models.CharField(blank=True, choices=[('Gyasi', 'Gyasi'), ('Value4Moni', 'Value4Moni')], default='Value4Moni', max_length=250, null=True),
        ),
    ]
