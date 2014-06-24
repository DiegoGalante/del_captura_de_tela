#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os

#recupera o usuário
pasta = os.environ["HOME"]
#monta o caminho
caminho = pasta+'/Imagens/'
#lista todos os arquivos dentro da pasta
lista = os.listdir(caminho)

#cont = 0

for x in lista:
	try:
		#Verifica se existe a palavra 'Captura' no X
		if 'Captura' in x:
			#Explode a frase pelos espaços para melhor modificá-la.
			nome_novo = x.split()
		
			if '-' not in nome_novo:
				#Monta a string com o formato necessário para a deleção.
				pontos = nome_novo[5].split(':')
				nome_arquivo_pronto = nome_novo[0]+"\\ "+nome_novo[1]+"\\ "+nome_novo[2]+"\\ "+nome_novo[3]+"\\ "+nome_novo[4]+"\\ "+pontos[0]+"\\:"+pontos[1]+"\\:"+pontos[2]+""
				#Comando que realiza a operação.
				os.system('rm '+caminho+nome_arquivo_pronto)
			else:
				pontos = nome_novo[5].split(':')
				nome_arquivo_pronto_ = nome_novo[0]+"\\ "+nome_novo[1]+"\\ "+nome_novo[2]+"\\ "+nome_novo[3]+"\\ "+nome_novo[4]+"\\ "+pontos[0]+"\\:"+pontos[1]+"\\:"+pontos[2]+"\\ "+nome_novo[6]+"\\ "+nome_novo[7]+""
				#Comando que realiza a operação.
				os.system('rm '+caminho+nome_arquivo_pronto_)

			cont = cont+1
		else:
			pass

	except Exception, e:
		pass

#print cont,'arquivo(s) deletados com sucesso! (:'
