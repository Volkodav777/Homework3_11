# Generated by Django 5.1.2 on 2024-10-09 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storemodels', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['surname'], 'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='last_name',
            new_name='surname',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='phone',
        ),
    ]
