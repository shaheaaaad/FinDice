# Generated by Django 4.2.20 on 2025-04-27 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_systemprompt'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bank_access_token',
            field=models.TextField(blank=True, null=True),
        ),
    ]
