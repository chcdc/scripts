#!/usr/bin/env python3.5
# 11/04/2017
# Carlos Carvalho

"""
Encontrar um termo dentro de um arquivo que esta dentro de uma pasta com diversos arquivos, geralmente do mesmo tipo.
Imprimir o arquivo encontrado, nome e conteudo
Copiar o arquivo para outra pasta para backup
Avisar que foi copiado
Finalizar e sair do programa
"""
import os
a=''
b=''
# Variaveis e diretorios
x=0
log=open('log/archive.log',"a+")
os.chdir('/home/carlos/scripts/shell')
# Recebe todos os arquivos contidos no diretorio citado
files=os.listdir()
search='\n' # Item a ser pesquisado

#search=input("Qual o termo a ser pesquisado?\n")
def search():
	# Verifica todos os arquivos da pasta
	while x<(len(files)):
		archive=files[x]
		# Abre todos os arquivos para leitura
		archiveon=open(archive, "r")
		# Faz a leitura do arquivo, linha por linha, arquivo por arquivo e cria uma lista
		for line in archiveon:
			line=archiveon.readlines()
			#print(line)
		# Procura a string informada
			indice=line.index(search)
			#print(indice)
		x+=1

def alert():
	print("Arquivo %s copiado para a pasta %s com sucesso" % (a,b))

alert()
