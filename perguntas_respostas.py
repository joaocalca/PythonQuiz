"""
Sistema de perguntas e respostas com dicionários
"""

print()
print('-' * 30, ' Quiz de perguntas e respostas com o tema  ' + '-' * 30)
print()

perguntas = {
   'Pergunta 1': {
       'pergunta': 'Qual a bandeira, entre os países abaixo, que não possui nenhum elemento na cor amarela? ',
       'respostas': {'a': 'Argentina', 'b': 'Brasil', 'c': 'Cuba'},
       'resposta_certa': 'c',
   },
   'Pergunta 2': {
       'pergunta': 'Qual é aproximadamente a população do estado de São Paulo? ',
       'respostas': {'a': '45 milhões', 'b': '28 milhões', 'c': '10 milhões'},
       'resposta_certa': 'a',
   },
   'Pergunta 3': {
       'pergunta': 'A capital dos Emirados Árabes Unidos é: ',
       'respostas': {'a': 'Arábia Saudita', 'b': 'Dubai', 'c': 'Abu Dhabi'},
       'resposta_certa': 'c',
   },
   'Pergunta 4': {
       'pergunta': 'O maior dos continentes, tanto em área como em população, é a: ',
       'respostas': {'a': 'América', 'b': 'Ásia', 'c': 'África'},
       'resposta_certa': 'b',
   },
   'Pergunta 5': {
       'pergunta': 'Qual o país cujo mapa lembra o formato de uma bota? ',
       'respostas': {'a': 'Inglaterra', 'b': 'Itália', 'c': 'França'},
       'resposta_certa': 'b',
   }
}

respostas_certas = 0

for pk, pv in perguntas.items():
   print(f'{pk}: {pv["pergunta"]}')

   for rk, rv in pv['respostas'].items():
       print(f'[{rk}]: {rv}')

   resposta_usuario = input('Informe a sua resposta: ')

   if resposta_usuario == pv['resposta_certa']:
       print('Parabéns a resposta está correta!!')
       respostas_certas += 1
   else:
       print('Resposta incorreta!!')

   print()

if respostas_certas != 0:
   qtd_perguntas = len(perguntas)
   porcentagem_acertos = respostas_certas / qtd_perguntas * 100
   print(f'Você acertou {respostas_certas} resposta(s).')
   print(f'Sua porcentagem de acertos foi de {porcentagem_acertos:.2f}%')
else:
   print('Você não acertou nenhuma resposta, tente novamente :(')
