# Generated by Django 4.0.2 on 2022-02-26 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etune', '0075_alter_scholar_app_sa_jsoncommit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scholar_app',
            name='sa_jsoncommit',
        ),
    ]