# Generated by Django 5.0.4 on 2024-04-06 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_member_created_at'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Member',
            new_name='Todo',
        ),
    ]
