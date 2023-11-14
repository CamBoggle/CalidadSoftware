# Generated by Django 4.2.1 on 2023-06-01 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Categoria')),
                ('nombreCategoria', models.CharField(blank=True, max_length=50, verbose_name='Nombre de Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='Codigo')),
                ('nombre', models.CharField(blank=True, max_length=50, verbose_name='Nombre')),
                ('descripcion', models.CharField(blank=True, max_length=250, verbose_name='Descripcion')),
                ('precio', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Precio')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mascotas.categoria', verbose_name='Categoria')),
            ],
        ),
    ]
