# Generated by Django 5.1.4 on 2025-02-26 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fhi_users", "0026_alter_userdomain_internal_phone_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="userdomain",
            name="business_name",
            field=models.CharField(default="oops", max_length=300),
            preserve_default=False,
        ),
    ]
