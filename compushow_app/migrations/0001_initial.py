# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=128)),
            ],
            options={
                'ordering': ['nombre'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Computista',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Edicion',
            fields=[
                ('anio', models.IntegerField(serialize=False, primary_key=True)),
                ('activa', models.BooleanField(default=False)),
                ('etapa', models.CharField(max_length=1, choices=[('0', 'CERRADO'), ('1', 'NOMINANDO'), ('2', 'FILTRANDO'), ('3', 'VOTANDO')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.ImageField(upload_to='directorioDondeSeVaAGuardar')),
                ('descripcion', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Nominacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categoria', models.ForeignKey(to='compushow_app.Categoria')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Nominado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('computista', models.ForeignKey(to='compushow_app.Computista')),
                ('foto', models.ForeignKey(to='compushow_app.Foto')),
                ('nominacion', models.ForeignKey(to='compushow_app.Nominacion')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='categoria',
            name='ganador',
            field=models.ForeignKey(to='compushow_app.Nominado', blank=True),
            preserve_default=True,
        ),
    ]
