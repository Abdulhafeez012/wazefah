# Generated by Django 4.0.2 on 2022-02-07 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wazefah', '0003_alter_userinformation_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='Gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=10),
        ),
    ]
