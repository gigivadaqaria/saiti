# Generated by Django 4.0.1 on 2022-01-29 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_userprofile_avatar'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Userprofile',
        ),
    ]
