# Generated by Django 4.2.5 on 2023-09-21 15:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "authentik_stages_authenticator_mobile",
            "0004_mobiledevice_last_checkin_mobiledevice_state",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="authenticatormobilestage",
            name="firebase_config",
            field=models.JSONField(default=dict, help_text="temp"),
        ),
    ]
