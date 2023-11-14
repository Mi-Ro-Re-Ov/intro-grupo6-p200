# Generated by Django 4.2.7 on 2023-11-13 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroRopa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('perfil_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.perfilusuario')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroBloqueador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('perfil_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.perfilusuario')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroAgua',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('cantidad_unidades', models.IntegerField()),
                ('tipo_agua', models.CharField(choices=[('V', 'Vasos'), ('B', 'Botellas')], max_length=1)),
                ('perfil_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.perfilusuario')),
            ],
        ),
    ]
