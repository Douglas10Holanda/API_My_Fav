# Generated by Django 4.2.4 on 2023-08-08 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('produtora', models.CharField(max_length=100)),
                ('temporadas', models.IntegerField()),
                ('ano_lancamento', models.IntegerField()),
                ('assistiu', models.BooleanField()),
                ('categorias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorias_series', to='categorias.categorias')),
            ],
        ),
    ]
