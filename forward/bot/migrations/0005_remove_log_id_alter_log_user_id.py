# Generated by Django 4.0.6 on 2023-03-18 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_rename_kurs_user_ctg_rename_level_user_subctg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='id',
        ),
        migrations.AlterField(
            model_name='log',
            name='user_id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
