# Generated by Django 5.1.4 on 2025-02-08 07:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fhi_users", "0012_patientdomainrelation_domain_and_more"),
        ("fighthealthinsurance", "0067_remove_denialdomainrelation_domain"),
    ]

    operations = [
        migrations.AddField(
            model_name="denialdomainrelation",
            name="domain",
            field=models.ForeignKey(
                default="1235",
                on_delete=django.db.models.deletion.CASCADE,
                to="fhi_users.userdomain",
            ),
            preserve_default=False,
        ),
    ]
