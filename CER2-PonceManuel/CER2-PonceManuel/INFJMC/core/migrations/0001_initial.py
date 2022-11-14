# Generated by Django 4.1.3 on 2022-11-13 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='correo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_correo', models.IntegerField()),
                ('n_recidencia', models.IntegerField()),
                ('Mensaje', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recidencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nu_recidencia', models.IntegerField()),
                ('n_correo', models.IntegerField()),
            ],
        ),
    ]
