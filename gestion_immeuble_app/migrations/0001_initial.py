# Generated by Django 5.0.6 on 2024-06-30 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Charge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_charge', models.CharField(max_length=120, verbose_name='Une Charge')),
            ],
        ),
    ]