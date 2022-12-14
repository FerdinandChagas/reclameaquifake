# Generated by Django 4.1 on 2022-09-02 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='reclame.usuario')),
                ('media_notas', models.FloatField(default=0.0)),
                ('ranking', models.IntegerField(default=0)),
            ],
            bases=('reclame.usuario', models.Model),
        ),
        migrations.CreateModel(
            name='Reclamacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=200)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reclame.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(verbose_name='data')),
                ('reclamacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reclame.reclamacao')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reclame.usuario')),
            ],
        ),
    ]
