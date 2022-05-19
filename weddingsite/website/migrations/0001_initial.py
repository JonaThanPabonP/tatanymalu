# Generated by Django 4.0.4 on 2022-05-19 02:56

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
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('imagen', models.ImageField(null=True, upload_to='fotos')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.categoria')),
            ],
        ),
    ]
