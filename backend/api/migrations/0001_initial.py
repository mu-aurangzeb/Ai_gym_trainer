# Generated by Django 4.0.1 on 2022-02-05 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('weight', models.PositiveIntegerField()),
                ('height', models.PositiveIntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=8)),
            ],
        ),
    ]
