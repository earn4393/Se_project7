# Generated by Django 4.0.1 on 2022-02-16 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etune', '0041_scholar_profile_sp_json_scholar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scholar_profile',
            name='sp_money_received_scholar',
        ),
        migrations.RemoveField(
            model_name='scholar_profile',
            name='sp_received_scholar',
        ),
        migrations.RemoveField(
            model_name='scholar_profile',
            name='sp_year_received_scholar',
        ),
    ]
