# Generated by Django 4.2.3 on 2023-07-24 09:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_alter_players_options_players_previous_club"),
    ]

    operations = [
        migrations.AlterField(
            model_name="players",
            name="first_name",
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name="players",
            name="last_name",
            field=models.CharField(max_length=20, unique=True),
        ),
    ]