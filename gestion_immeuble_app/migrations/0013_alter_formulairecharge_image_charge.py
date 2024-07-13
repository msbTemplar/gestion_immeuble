# Generated by Django 5.0.6 on 2024-07-13 11:18

import gestion_immeuble_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_immeuble_app', '0012_formulairecotization_codeformcotiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulairecharge',
            name='image_charge',
            field=models.FileField(blank=True, null=True, upload_to='uploads/', validators=[gestion_immeuble_app.models.validate_file_extension], verbose_name='Fichier de charge'),
        ),
    ]
