# Generated by Django 4.1.1 on 2022-09-19 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("entrenamiento", "0013_timecap_detail"),
    ]

    operations = [
        migrations.RemoveField(model_name="timecap_detail", name="Nombre",),
        migrations.AlterField(
            model_name="timecap_detail",
            name="name",
            field=models.CharField(
                choices=[("NM", "Nombre")], default="NM", max_length=100
            ),
        ),
    ]