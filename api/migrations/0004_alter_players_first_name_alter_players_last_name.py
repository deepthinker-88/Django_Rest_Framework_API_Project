# Generated by Django 4.2.3 on 2023-07-24 11:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0003_alter_players_first_name_alter_players_last_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="players",
            name="first_name",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="players",
            name="last_name",
            field=models.CharField(max_length=20),
        ),
    ]
