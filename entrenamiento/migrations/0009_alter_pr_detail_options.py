# Generated by Django 4.1.1 on 2022-09-18 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("entrenamiento", "0008_alter_pr_detail_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="pr_detail", options={"ordering": ("name", "-date")},
        ),
    ]