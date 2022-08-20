# Generated by Django 4.1 on 2022-08-20 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaPalavra',
            fields=[
                ('nome', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Palavras',
            fields=[
                ('id_palavra', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255, unique=True)),
                ('categoria', models.CharField(max_length=255)),
            ],
        ),
    ]
