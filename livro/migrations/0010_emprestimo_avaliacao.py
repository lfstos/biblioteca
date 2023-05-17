# Generated by Django 4.2 on 2023-05-16 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0009_rename_deta_devolucao_emprestimo_data_devolucao'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimo',
            name='avaliacao',
            field=models.CharField(choices=[('P', 'Péssimo'), ('R', 'Ruim]'), ('B', 'Bom'), ('O', 'Ótimo')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
    