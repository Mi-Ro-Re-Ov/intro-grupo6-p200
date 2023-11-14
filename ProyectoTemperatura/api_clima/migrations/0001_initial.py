# Generated by Django 4.2.7 on 2023-11-13 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InformacionClimatica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(max_length=255)),
                ('temperatura', models.FloatField()),
                ('descripcion', models.TextField()),
            ],
        ),
    ]
