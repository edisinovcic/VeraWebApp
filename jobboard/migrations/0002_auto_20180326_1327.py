# Generated by Django 2.0.3 on 2018-03-26 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionhistory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to=settings.AUTH_USER_MODEL),
        ),
    ]
