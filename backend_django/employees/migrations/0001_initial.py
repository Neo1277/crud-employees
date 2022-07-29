# Generated by Django 4.0.6 on 2022-07-29 21:00

from django.db import migrations, models
import employees.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('id', employees.models.UnsignedAutoField(primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date and time when the register was created')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date and time when the register was updated')),
            ],
        ),
    ]
