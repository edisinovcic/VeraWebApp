# Generated by Django 2.0.3 on 2018-06-28 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0001_initial'),
        ('interview', '0007_auto_20180628_1059'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='scheduledmeeting',
            unique_together={('action_interview', 'candidate')},
        ),
    ]
