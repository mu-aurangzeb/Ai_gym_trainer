# Generated by Django 4.0.1 on 2022-04-07 11:57

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_info',
            name='diet_plan',
            field=jsonfield.fields.JSONField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='user_info',
            name='exercise_plan',
            field=jsonfield.fields.JSONField(max_length=1000, null=True),
        ),
    ]
