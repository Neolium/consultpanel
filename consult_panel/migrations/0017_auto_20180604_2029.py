# Generated by Django 2.0.5 on 2018-06-04 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consult_panel', '0016_auto_20180531_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centreformation',
            name='siret',
            field=models.CharField(blank=True, max_length=14, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='centreformation',
            name='telephone',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]