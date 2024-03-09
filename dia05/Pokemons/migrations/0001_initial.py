# Generated by Django 5.0.3 on 2024-03-09 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeDoPokemon', models.CharField(max_length=20, verbose_name='Nome do Pokemon')),
                ('habilidade', models.CharField(blank=True, max_length=30, null=True, verbose_name='Habilidades')),
                ('altura', models.IntegerField(blank=True, null=True, verbose_name='Altura')),
                ('pokedex_id', models.IntegerField(blank=True, null=True, verbose_name='Id na Pokedex')),
                ('peso', models.IntegerField(blank=True, null=True, verbose_name='Peso')),
            ],
        ),
    ]
