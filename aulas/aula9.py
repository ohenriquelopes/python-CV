# MANIPULANDO TEXTO

frase = 'Curso em video python'

frase[9]
frase[9:13]
frase[9:21:2] #pega o range e pula de 2 em 2
frase[:5] #indica o final 
frase[15:] #indica o inicio mas nao o final
frase[9::3] #inicia no 9 e nao o final e pula de 3 em 3

#ANALISE de string

len(frase)
frase.count('o') #conta quantas vezes aparece a letra O
frase.count('o',0,13) #mesma coisa da anterior mas com fatiamento
frase.find('deo') #indica o indice de onde comecou o 'deo'
frase.find('android') #retorna -1, signifca que nao foi encontrada
print('Curso' in frase) # retona true or false
frase.replace('Python','Android')
frase.upper()
frase.lower()
frase.capitalize()
frase.title()
frase.strip() #remove os espacos inuteis no inicio e no fim da string
frase.rstrip() #remove do lado direito
frase.lstrip() #remove do lado esquerdo
print(frase.upper().count('O')) #exemplo de como da para concater os comandos

# Divisao

frase.split() #refaz os indices no caso do exemplo 4 itens em 1 lista

#juncao

'-'.join(frase)

print("""
escrever em varias linhas
como exemplo
retonar em 1 print so
        """)


