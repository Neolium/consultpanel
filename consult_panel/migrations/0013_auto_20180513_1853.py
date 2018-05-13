# Generated by Django 2.0.5 on 2018-05-13 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consult_panel', '0012_entreprise_siret'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centreformation',
            name='adresse',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='centreformation',
            name='code_postal',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='centreformation',
            name='siret',
            field=models.CharField(max_length=14, unique=True),
        ),
        migrations.AlterField(
            model_name='centreformation',
            name='telephone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='centreformation',
            name='ville',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='client',
            name='catalogue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consult_panel.Catalogue'),
        ),
        migrations.AlterField(
            model_name='client',
            name='entreprise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consult_panel.Entreprise'),
        ),
        migrations.AlterField(
            model_name='cours',
            name='localisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consult_panel.Localisation'),
        ),
        migrations.AlterField(
            model_name='cours',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consult_panel.Session'),
        ),
        migrations.AlterField(
            model_name='entreprise',
            name='adresse',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='entreprise',
            name='code_postal',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='entreprise',
            name='siret',
            field=models.CharField(max_length=14, unique=True),
        ),
        migrations.AlterField(
            model_name='entreprise',
            name='telephone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='entreprise',
            name='ville',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='formation',
            name='prix_ht',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consult_panel.Client'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consult_panel.Session'),
        ),
        migrations.AlterField(
            model_name='localisation',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consult_panel.Profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='centre_formation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consult_panel.CentreFormation'),
        ),
    ]
