# Generated by Django 4.0.2 on 2022-02-25 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etune', '0063_file_models_fm_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholar_app',
            name='sa_person',
            field=models.IntegerField(default=0),
        ),
    ]
