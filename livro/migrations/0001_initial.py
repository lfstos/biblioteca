# Generated by Django 4.2 on 2023-04-25 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=30)),
                ('co_autor', models.CharField(blank=True, max_length=30, null=True)),
                ('nome_emprestado', models.CharField(max_length=30)),
                ('emprestado', models.BooleanField(default=False)),
                ('data_cadastro', models.DateField(auto_now_add=True)),
                ('data_emprestimo', models.DateField(default=False)),
                ('deta_devolucao', models.DateField(default=False)),
                ('tempo_duracao', models.DateField()),
            ],
        ),
    ]
