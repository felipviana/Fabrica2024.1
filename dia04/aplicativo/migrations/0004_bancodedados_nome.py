# Generated by Django 5.0.3 on 2024-03-08 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicativo', '0003_remove_bancodedados_nome_bancodedados_bairro_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bancodedados',
            name='nome',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome'),
        ),
    ]
