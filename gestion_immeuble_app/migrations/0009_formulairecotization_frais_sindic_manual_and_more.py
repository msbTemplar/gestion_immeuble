# Generated by Django 5.0.6 on 2024-07-07 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_immeuble_app', '0008_alter_formulairecotization_frais_sindic'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulairecotization',
            name='frais_sindic_manual',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Frais Sindic Manual'),
        ),
        migrations.AlterField(
            model_name='formulairecotization',
            name='frais_sindic',
            field=models.CharField(blank=True, choices=[('', ''), ('----', '----'), ('Frais Sindic', 'Frais Sindic')], max_length=120, null=True, verbose_name='Frais Sindic'),
        ),
    ]
