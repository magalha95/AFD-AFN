#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Codifing by: Ítalo Magalhães da Silva 
#Email: italo.ufsj@gmail.com

import sys

#Função que valida a Quadrupla
def valida_maquina(maquina):
    return len(maquina) == 4

#Função para validar se cada caracter da palavra se encontra no alfabeto
def valida_palavra(alfabeto, palavra):
    for i in palavra:
        if i not in alfabeto:
            return False
    return True

#Função recebe a quadrupla representada pela maquina e uma palavra para ser processada
def processa_palavra(maquina, palavra):
    
    #Caso a quantidade de elementos da tupla for menor que 4 ou a palavra não consiga ser validada
    if not valida_maquina(maquina) or not valida_palavra(maquina[0],palavra):
        return False

    # Processamento do automato.
    novoestado = maquina[2]
    for char in palavra:
        novoestado = maquina[1][novoestado][char]
        
    return (novoestado in maquina[3])

if __name__ == '__main__':

    #Define o alfabeto 
    alfabeto = ['0', '1']
    #Define a função de transição
    '''
        Ex: (q1,0)=q1
            (q1,1)=q2
            (q2,0)=q1
            (q2,1)=q2
    '''
    funcao_transicao = {'q1' : {'0' : 'q1', '1' : 'q2'},
                        'q2' : {'0' : 'q1', '1' : 'q2'}}

    #Define o estado incial
    estado_inicial = 'q1'
    #Define o conjunto de estados finais
    estados_finais = ['q1']

    #Define uma quadrupla. É uma quadrupla pois a função transição já está mapeada
    maquina = (alfabeto, funcao_transicao, estado_inicial, estados_finais)
    
    #Abertura do arquivo de Leitura contendo todas as palavras para serem processadas
    arquivoEntrada= sys.argv[1]
    arquivo = open(arquivoEntrada,'r')    
    palavras = arquivo.read()
    #Quebra a lista contendo todas as palavras no "\n"
    palavras = palavras.split('\n')
    #Abre arquivo saida para salvar as respostas computadas pelo automato
    arquivoSaida = open('resultadoPalavrasAFD.txt','w')
    respostaFinal=[]

    print "Processando as Palavras do Arquivo..."
    for palavra in palavras:
        resultado = processa_palavra(maquina, palavra)
        palavraResultado= palavra + " " + str(resultado) + "\n"
        respostaFinal.append(palavraResultado)

    print "Salvando resultados"
    #Salva as palavras no arquivo 
    arquivoSaida.writelines(respostaFinal)