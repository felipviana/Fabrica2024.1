# Generated by Django 5.0.3 on 2024-03-08 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicativo', '0002_alter_bancodedados_nome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bancodedados',
            name='nome',
        ),
        migrations.AddField(
            model_name='bancodedados',
            name='bairro',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Bairro do usuário'),
        ),
        migrations.AddField(
            model_name='bancodedados',
            name='complemento',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Complemento do usuário'),
        ),
        migrations.AddField(
            model_name='bancodedados',
            name='localidade',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Localidade do usuário'),
        ),
        migrations.AddField(
            model_name='bancodedados',
            name='logradouro',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Logradouro do usuário'),
        ),
        migrations.AddField(
            model_name='bancodedados',
            name='uf',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Estado do usuário'),
        ),
    ]
