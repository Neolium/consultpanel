# Generated by Django 2.0.5 on 2018-05-30 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consult_panel', '0015_auto_20180528_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_list', to='consult_panel.Session'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incription_list', to='consult_panel.Client'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incription_list', to='consult_panel.Session'),
        ),
    ]
