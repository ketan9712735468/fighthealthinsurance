# Generated by Django 5.1.5 on 2025-03-05 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fighthealthinsurance", "0084_appeal_fax_denial_date_of_service_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="appeal",
            name="success",
            field=models.BooleanField(default=False, null=True),
        ),
    ]
