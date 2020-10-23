funcionarios = [
    {
        'nome': 'Bruno',
        'vendas': 0,
        'equipe': ['Ana', 'Diandra', 'Nico'],
    },
    {
        'nome': 'Ana',
        'vendas': 300,
        'equipe': ['Bia', 'Camila'],
    },
    {
        'nome': 'Diandra',
        'vendas': 450,
        'equipe': ['Maga', 'Fábio'],
    },
    {
        'nome': 'Nico',
        'vendas': 500,
        'equipe': ['Lucas', 'Vini'],
    },
    {
        'nome': 'Bia',
        'vendas': 100,
        'equipe': [],
    },
    {
        'nome': 'Camila',
        'vendas': 350,
        'equipe': [],
    },
    {
        'nome': 'Maga',
        'vendas': 200,
        'equipe': [],
    },
    {
        'nome': 'Fábio',
        'vendas': 210,
        'equipe': [],
    },
    {
        'nome': 'Lucas',
        'vendas': 150,
        'equipe': [],
    },
    {
        'nome': 'Vini',
        'vendas': 100,
        'equipe': [],
    },
]

def retornar_salario(funcionarios, funcionario):
    for func in funcionarios:
        if func['nome'] == funcionario:
            dados_funcionario = func
    time = dados_funcionario['equipe']
    if len(time) == 0:
        salario = dados_funcionario['vendas']*0.95 #Cálculo de salário para quem não é líder

    tamanho_da_equipe = len(time)
    contador_time = 0
    while contador_time < tamanho_da_equipe:
        if func['nome'] == time[contador_time]:
            salario = salario + func['vendas']

        salario = dados_funcionario['vendas']


retornar_salario(funcionarios, 'Camila')

