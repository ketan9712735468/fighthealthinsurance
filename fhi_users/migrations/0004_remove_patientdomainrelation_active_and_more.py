# Generated by Django 5.1.4 on 2025-02-06 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fhi_users", "0003_professionaldomainrelation_pending_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="patientdomainrelation",
            name="active",
        ),
        migrations.AddField(
            model_name="userdomain",
            name="stripe_subscription_id",
            field=models.CharField(max_length=300, null=True),
        ),
    ]
