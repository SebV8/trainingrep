# Generated by Django 4.1.1 on 2022-09-18 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("entrenamiento", "0003_pr_detail_delete_pr"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pr_detail",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
