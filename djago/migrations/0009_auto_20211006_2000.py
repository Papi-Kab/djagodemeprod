# Generated by Django 3.1.7 on 2021-10-06 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djago', '0008_auto_20210623_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compte',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='projet',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='projet',
            name='secteur',
            field=models.CharField(max_length=50, verbose_name="Secteur d'Activité"),
        ),
        migrations.AlterField(
            model_name='projet',
            name='statut',
            field=models.CharField(choices=[('SDI', "Stade d'Idée"), ('EGN', 'En Gestation'), ('JLC', 'Juste Lancé'), ('EAE', 'En Activité'), ('C', 'Cloturé')], max_length=30, verbose_name='Statut du Projet'),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
