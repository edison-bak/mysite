# Generated by Django 4.0.3 on 2023-11-13 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toto', '0014_remove_choice_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='choice',
        ),
    ]
