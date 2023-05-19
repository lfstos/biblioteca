from django import template
from datetime import date


register = template.Library()


@register.filter
def mostra_duracao(data_emprestimo, data_devolucao):
    if isinstance(data_emprestimo, date) and isinstance(data_devolucao, date):
        dia = (data_devolucao - data_emprestimo).days
        if dia == 1:
            return f'{dia} dia'
        return f'{dia} dias'
