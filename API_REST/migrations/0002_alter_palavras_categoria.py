# Generated by Django 4.1 on 2022-08-20 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API_REST', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='palavras',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='API_REST.categoriapalavra'),
        ),
    ]
