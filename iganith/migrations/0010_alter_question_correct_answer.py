# Generated by Django 4.2.5 on 2023-10-31 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iganith', '0009_useranswer_just_answered_alter_useranswer_answered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct_answer',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
