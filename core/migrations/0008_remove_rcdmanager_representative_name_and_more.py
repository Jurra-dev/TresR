# Generated by Django 5.1.1 on 2025-04-11 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_logisticoperator_main_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rcdmanager',
            name='representative_name',
        ),
        migrations.AlterField(
            model_name='rcdmanager',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
