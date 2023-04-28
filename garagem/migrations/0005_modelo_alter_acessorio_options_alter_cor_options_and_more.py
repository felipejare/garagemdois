# Generated by Django 4.1.7 on 2023-04-28 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0004_acessorio_cor_veiculo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('nacionalidade', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Modelos',
            },
        ),
        migrations.AlterModelOptions(
            name='acessorio',
            options={'verbose_name': 'Acessório'},
        ),
        migrations.AlterModelOptions(
            name='cor',
            options={'verbose_name_plural': 'Cores'},
        ),
        migrations.AlterModelOptions(
            name='veiculo',
            options={'verbose_name': 'Veículo'},
        ),
    ]
