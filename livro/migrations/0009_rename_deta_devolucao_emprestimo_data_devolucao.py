# Generated by Django 4.1.7 on 2023-05-03 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0008_alter_emprestimo_nome_emprestado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emprestimo',
            old_name='deta_devolucao',
            new_name='data_devolucao',
        ),
    ]
