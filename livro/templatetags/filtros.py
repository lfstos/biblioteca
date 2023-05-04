from django import template

register = template.Library()


@register.filter
def mostra_duracao(data_emprestimo, data_devolucao):
    # val1 = datetime.strptime(data_emprestimo, '%Y-%m-%d')
    # val2 = datetime.strptime(data_devolucao, '%Y-%m-%d')
    return (data_emprestimo - data_devolucao).days
