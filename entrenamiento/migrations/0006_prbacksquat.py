# Generated by Django 4.1.1 on 2022-09-18 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("entrenamiento", "0005_rm_detail"),
    ]

    operations = [
        migrations.CreateModel(
            name="PrBackSquat",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("weight", models.CharField(max_length=100)),
                ("date", models.DateField()),
            ],
        ),
    ]
