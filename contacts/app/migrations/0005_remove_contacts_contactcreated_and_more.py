# Generated by Django 4.1.1 on 2022-10-07 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_contacts_contactcreated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='ContactCreated',
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='ContactEmail',
        ),
    ]
