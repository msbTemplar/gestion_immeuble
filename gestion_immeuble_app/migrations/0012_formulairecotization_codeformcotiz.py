# Generated by Django 5.0.6 on 2024-07-13 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_immeuble_app', '0011_formulairepconcierge_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulairecotization',
            name='codeFormCotiz',
            field=models.IntegerField(blank=True, null=True, verbose_name='Code'),
        ),
    ]
