# Generated by Django 4.0.4 on 2022-11-08 17:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('iohunt', '0004_alter_player_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='endTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='userProfile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
