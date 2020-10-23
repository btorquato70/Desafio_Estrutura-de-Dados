alunos = [
    {
        'nome': 'João',
        'respostas': [
            'C',
            'A',
            'D',
            'B',
            'D'
        ]
    },
    {
       'nome': 'Maria',
        'respostas': [
            'C',
            'D',
            'D',
            'D',
            'D'
        ]
    }
]

gabarito = [
    'A',
    'A',
    'B',
    'A',
    'A'
]

peso = [
    3,
    2,
    1,
    1,
    3
]

def calcular_nota(lista_alunos, gabarito, peso, posicao_aluno):
    aluno = lista_alunos[posicao_aluno]
    lista_respostas = aluno['respostas']
    nome_aluno = aluno['nome']
    contador_gabarito = 0
    contador_peso = 0
    nota_aluno = 0
    for resposta in lista_respostas:
        if resposta == gabarito[contador_gabarito]:
            nota_aluno = nota_aluno + peso[contador_peso]
        contador_gabarito = contador_gabarito + 1
        contador_peso = contador_peso + 1
    print(f'A nota do(a) aluno(a) {nome_aluno} é {nota_aluno}')

print(calcular_nota(alunos, gabarito, peso, 0))
print(calcular_nota(alunos, gabarito, peso, 1))