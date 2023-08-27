# Generated by Django 4.2.4 on 2023-08-16 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startgame', '0002_alter_gamedata_current_score_alter_gamedata_lastgame'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamedata',
            name='current_score',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='gamedata',
            name='lastgame',
            field=models.DateField(default=0, null=True),
        ),
    ]
