# Generated by Django 4.0.1 on 2022-02-13 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinformation',
            old_name='ProfilePick',
            new_name='ProfilePic',
        ),
    ]
