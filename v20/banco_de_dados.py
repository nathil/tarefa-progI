"""
A função carregar_banco_de_dados realiza a leitura de todas as linhas do aquivo. Observe
que o modo de operação para manipulação do arquivo é o R, indicando que será realizada
manipulação de leitura. Para ler todas as linhas do arquivo, utilizamos a função
readlines() que retorna uma lista de string. Estamos iterando cada linha do arquivo,
e realizando o mapeamento com a função map_usuario(). No final do mapeamento, temos
uma lista de dicionário, em que cada elemento é um dicionário com as chaves nome e
telefone.
No escopo da função map_usuario(linha) estamos utilizando a função split para construir
uma lista de string a partir da linha. Estamos considerando como critério de split a 
vírgula. Assim, a string 'Renato,123' gera a lista ['Renato', '123']. Considerando os
valores da lista, montamos o dicionário com chave nome e telefone.
"""

def carregar_banco_de_dados():
    with open('banco_de_dados', mode='r') as bd:        
        return [
            map_usuario(linha)
            for linha in bd.readlines() 
        ]

def map_usuario(linha):
    values = linha.split(',')    
    return {
        'nome': values[0].strip(),
        'telefone': values[1].strip(),
        'cpf':values[2].strip(),
        'endereco':values[3].strip(),
        'email':values[4].strip(),
        'sexo':values[5].strip(),
        'uf':values[6].strip()
    }

"""
A função salvar está manipulando o arquivo com o modo de operação A, indicando que iremos
acrescentar conteúdo ao arquivo já existente. Estamos escrevendo uma nova linha no
arquivo, utilizando a função write. Esta função recebe como argumento uma string.
Observe que a string passada como argumento termina com \n. Isso né necessário para poder
quebrar a linha. No retorno da função salvar, estamos chamando a função 
carregar_banco_de_dados() que retorna a lista de dicionários.

"""
def salvar(usuario):    
    with open('banco_de_dados', mode='a') as bd:        
        bd.write(f"{usuario['nome']},{usuario['telefone']},{usuario['cpf']},{usuario['endereco']},{usuario['email']},{usuario['sexo']},{usuario['uf']}\n")
    return carregar_banco_de_dados()


"""
A função atualizar_banco_de_dados está manipulando o arquivo com o modo de operação W,
indicando que o conteúdo do arquivo será zerado e reescrito. Estamos iterando a lista
de dicionário e utiizando a função write para escrever as linhas do arquivo.
"""
def atualizar_banco_de_dados(lista):
    with open('banco_de_dados', mode='w') as bd:
        for usuario in lista:
            bd.write(f"{usuario['nome']},{usuario['telefone']},{usuario['cpf']},{usuario['endereco']},{usuario['email']},{usuario['sexo']},{usuario['uf']}\n")    


