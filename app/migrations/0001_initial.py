# Generated by Django 4.2.5 on 2023-09-26 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Continente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('continente', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('site', models.URLField()),
                ('insta', models.URLField()),
                ('face', models.URLField()),
                ('twitter', models.URLField()),
                ('nacionalidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pais')),
            ],
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('duracao', models.IntegerField()),
                ('sinopse', models.TextField()),
                ('site_oficial', models.URLField()),
                ('data_lancamento', models.DateField()),
                ('nota_avaliacao', models.DecimalField(decimal_places=1, max_digits=3)),
                ('diretor', models.ManyToManyField(related_name='dirigiu_series', to='app.pessoa')),
                ('genero', models.ManyToManyField(to='app.genero')),
                ('pais', models.ManyToManyField(to='app.pais')),
            ],
        ),
        migrations.CreateModel(
            name='Temporada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.serie')),
            ],
        ),
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('duracao', models.IntegerField()),
                ('sinopse', models.TextField()),
                ('site_oficial', models.URLField()),
                ('data_lancamento', models.DateField()),
                ('nota_avaliacao', models.DecimalField(decimal_places=1, max_digits=3)),
                ('diretor', models.ManyToManyField(related_name='dirigiu_filmes', to='app.pessoa')),
                ('genero', models.ManyToManyField(to='app.genero')),
                ('pais', models.ManyToManyField(to='app.pais')),
            ],
        ),
        migrations.CreateModel(
            name='Episodio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('duracao', models.IntegerField()),
                ('data_disponibilizacao', models.DateField()),
                ('temporada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.temporada')),
            ],
        ),
        migrations.CreateModel(
            name='Ator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('filmes', models.ManyToManyField(related_name='atores', to='app.filme')),
            ],
        ),
    ]