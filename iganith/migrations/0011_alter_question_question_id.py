# Generated by Django 4.2.5 on 2023-10-31 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iganith', '0010_alter_question_correct_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_id',
            field=models.IntegerField(unique=True),
        ),
    ]
