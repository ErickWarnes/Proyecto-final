# Generated by Django 4.1.4 on 2022-12-22 02:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo_consulta', models.IntegerField(choices=[[0, 'Felicitaciones'], [1, 'Sugerencias'], [2, 'Consultas']])),
                ('mensaje', models.TextField()),
                ('avisos', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('subtitulo', models.CharField(blank=True, max_length=150, null=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('texto', models.TextField()),
                ('activo', models.BooleanField(default=True)),
                ('imagen', models.ImageField(blank=True, default='noticia/default.png', null=True, upload_to='noticia')),
                ('publicado', models.DateField(default=django.utils.timezone.now)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='noticias.categoria')),
            ],
            options={
                'ordering': ('-publicado',),
            },
        ),
    ]