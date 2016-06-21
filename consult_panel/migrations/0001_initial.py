# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-21 12:36
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('catalogue', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='consult_panel.Catalogue')),
            ],
        ),
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_cours_debut', models.DateTimeField(default=datetime.datetime.now)),
                ('date_cours_fin', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='EmailForBeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entreprise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('siret', models.CharField(default='DEFAULT_SIRET', max_length=14, unique=True)),
                ('adresse', models.CharField(default='DEFAULT_ADDR', max_length=255)),
                ('code_postal', models.CharField(default='DEFAULT_CP', max_length=10)),
                ('telephone', models.CharField(default='DEFAULT_PHONE', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('prix_ht', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('prix_ttc', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Localisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('latitude', models.CharField(max_length=200)),
                ('longitude', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PreferenceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liste_catalogues', models.ManyToManyField(to='consult_panel.Catalogue')),
                ('liste_entreprises', models.ManyToManyField(to='consult_panel.Entreprise')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consult_panel.Formation')),
            ],
        ),
        migrations.AddField(
            model_name='preference',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consult_panel.PreferenceType'),
        ),
        migrations.AddField(
            model_name='localisation',
            name='profile',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='consult_panel.Profile'),
        ),
        migrations.AddField(
            model_name='inscription',
            name='session',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='consult_panel.Session'),
        ),
        migrations.AddField(
            model_name='cours',
            name='localisation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='consult_panel.Localisation'),
        ),
        migrations.AddField(
            model_name='cours',
            name='session',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='consult_panel.Session'),
        ),
        migrations.AddField(
            model_name='client',
            name='entreprise',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='consult_panel.Entreprise'),
        ),
        migrations.AddField(
            model_name='catalogue',
            name='liste_formations',
            field=models.ManyToManyField(blank=True, to='consult_panel.Formation'),
        ),
    ]
