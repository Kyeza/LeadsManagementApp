# Generated by Django 3.0.1 on 2019-12-18 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Leads',
            new_name='Lead',
        ),
    ]
