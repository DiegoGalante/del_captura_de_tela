#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os

pasta = os.environ["HOME"]

try:
	download = os.listdir(pasta+"/Downloads/")

	if 'del_captura_de_tela-master' not in download:
		if 'del_captura_de_tela-master.zip' in download:
			try:
				os.system("cd $HOME/Downloads/ && unzip del_captura_de_tela-master.zip")

				diretorio = os.listdir('/etc/')
				if 'script' not in diretorio:
					try:
						os.system('sudo mkdir /etc/script/')
						print 'Diretório criado com sucesso!'
								
						diretorio = os.listdir('/etc/')
						if 'script' in diretorio:
							try:
								os.system('cd $HOME/Downloads/del_captura_de_tela-master/ && sudo mv del_captura_de_tela.py /etc/script/')
								print 'Arquivo adicionado na pasta com sucesso!'

								diretorio_script = os.listdir('/etc/script/')
								if 'del_captura_de_tela.py' in diretorio_script:
									try:
										os.system('cd $HOME/Downloads/ && rm -r del_captura_de_tela-master/')
										print 'Arquivo atualizado com sucesso!\n'
										print 'Insira o comando na ultima linha crontab para agendar o processo no sistema!'
										print 'Comando: */1 * * * * python /etc/script/del_captura_de_tela.py\n'

										comando = "*/1 * * * * python /etc/script/del_captura_de_tela.py"

									except Exception, e:
										print 'Não foi possível deletar a pasta del_captura_de_tela-master/ em $HOME/Downloads'

								else:
									try:
										os.system('cd $HOME/Downloads/ && rm -r del_captura_de_tela-master/')
							
										print 'Instalação dos arquivos concluída com sucesso!\n'
										print 'Insira o comando na ultima linha crontab para agendar o processo no sistema!'
										print 'Comando: */1 * * * * python /etc/script/del_captura_de_tela.py\n'
							
										comando = "*/1 * * * * python /etc/script/del_captura_de_tela.py"

									except Exception, e:
										pass


							except Exception, e:
								print 'Não foi possível mover o arquivo da pasta $HOME/Downloads/del_captura_de_tela-master/ '
						else:
							pass
							#print 'Arquivo del não existe ema /etc/script/'
					except Exception, e:
						print 'Não foi possível criar a pasta script/ em /etc/'
				else:
					diretorio_script = os.listdir('/etc/script/')
					if 'del_captura_de_tela.py' not in diretorio_script:
						try:
							os.system('cd $HOME/Downloads/ && rm -r del_captura_de_tela-master/')
							
							print 'Instalação dos arquivos concluída com sucesso!\n'
							print 'Insira o comando na ultima linha crontab para agendar o processo no sistema!'
							print 'Comando: */1 * * * * python /etc/script/del_captura_de_tela.py\n'
							
							comando = "*/1 * * * * python /etc/script/del_captura_de_tela.py"

						except Exception, e:
							pass
							#print 'Não foi possível deletar a pasta del_captura_de_tela-master/ em $HOME/Downloads'

					else:
						try:
							os.system('cd $HOME/Downloads/ && rm -r del_captura_de_tela-master/')
						
							print '\nArquivo atualizado com sucesso!!'
							print 'Insira o comando na ultima linha crontab para agendar o processo no sistema!'
							print 'Comando: */1 * * * * python /etc/script/del_captura_de_tela.py\n'
							
							comando = "*/1 * * * * python /etc/script/del_captura_de_tela.py"
						except Exception, e:
							pass
							#print 'Não foi possível deletar a pasta del_captura_de_tela-master/ em $HOME/Downloads'

			except Exception, e:
				print 'Não foi possível descompactar o arquivo.'

		else:
			#print 'Arquivo del_captura_de_tela-master.zip não existe em $HOME/Downloads/'
			pass
	else:
		diretorio = os.listdir('/etc/')
		if 'script' not in diretorio:
			try:
				os.system('sudo mkdir /etc/script/')
				print 'Diretório criado com sucesso!'
								
				diretorio = os.listdir('/etc/')
				if 'script' in diretorio:
					try:
						os.system('cd $HOME/Downloads/del_captura_de_tela-master/ && sudo mv del_captura_de_tela.py /etc/script/')
						print 'Arquivo adicionado na pasta com sucesso!'

						diretorio_script = os.listdir('/etc/script/')
						if 'del_captura_de_tela.py' in diretorio_script:
							try:
								os.system('cd $HOME/Downloads/ && rm -r del_captura_de_tela-master/')
								print 'Instalação dos arquivos concluída com sucesso!\n'
								print 'Insira o comando na ultima linha crontab para agendar o processo no sistema!'
								print 'Comando: */1 * * * * python /etc/script/del_captura_de_tela.py\n'

								comando = "*/1 * * * * python /etc/script/del_captura_de_tela.py"

							except Exception, e:
								print 'Não foi possível deletar a pasta del_captura_de_tela-master/ em $HOME/Downloads'
						else:
							try:
								os.system('cd $HOME/Downloads/ && rm -r del_captura_de_tela-master/')
							
								print 'Instalação dos arquivos concluída com sucesso!\n'
								print 'Insira o comando na ultima linha crontab para agendar o processo no sistema!'
								print 'Comando: */1 * * * * python /etc/script/del_captura_de_tela.py\n'
							
								comando = "*/1 * * * * python /etc/script/del_captura_de_tela.py"

							except Exception, e:
								pass


					except Exception, e:
								pass
				else:
					pass
					#print 'Arquivo del não existe ema /etc/script/'
			except Exception, e:
				print 'Não foi possível criar a pasta script/ em /etc/'

		else:
			try:

				os.system('cd $HOME/Downloads/del_captura_de_tela-master/ && sudo mv del_captura_de_tela.py /etc/script/')
				print 'Arquivo adicionado na pasta com sucesso!'

				diretorio_script = os.listdir('/etc/script/')
				if 'del_captura_de_tela.py' in diretorio_script:
					try:
						os.system('cd $HOME/Downloads/ && rm -r del_captura_de_tela-master/')
							
						print 'Arquivo atualizado com sucesso!\n'
						print 'Insira o comando na ultima linha crontab para agendar o processo no sistema!'
						print 'Comando: */1 * * * * python /etc/script/del_captura_de_tela.py\n'
							
						comando = "*/1 * * * * python /etc/script/del_captura_de_tela.py"

					except Exception, e:
						pass
				
				else:
					try:
						os.system('cd $HOME/Downloads/ && rm -r del_captura_de_tela-master/')
							
						print 'Instalação dos arquivos concluída com sucesso!\n'
						print 'Insira o comando na ultima linha crontab para agendar o processo no sistema!'
						print 'Comando: */1 * * * * python /etc/script/del_captura_de_tela.py\n'
							
						comando = "*/1 * * * * python /etc/script/del_captura_de_tela.py"
							#print 'Não foi possível deletar a pasta del_captura_de_tela-master/ em $HOME/Downloads'

					except Exception, e:
						pass

			except Exception, e:
						print 'Não foi possível mover o arquivo da pasta $HOME/Downloads/del_captura_de_tela-master/ '
						
except Exception, e:
	print 'Falha crítica! Informe o criador do script ou algum programador que possa resolver.'
