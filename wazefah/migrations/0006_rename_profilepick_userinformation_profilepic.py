# Generated by Django 4.0.1 on 2022-02-09 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wazefah', '0005_rename_experiance_userinformation_experience'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinformation',
            old_name='ProfilePic',
            new_name='ProfilePic',
        ),
    ]
