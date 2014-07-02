#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

try:
	pasta = os.environ["HOME"]
	user = pasta.split('/')

	download = os.listdir(pasta+"/Downloads/")

	if 'del_captura_de_tela-master' not in download:
		if 'del_captura_de_tela-master.zip' in download:
			try:
				os.system("cd $HOME/Downloads/ && unzip del_captura_de_tela-master.zip")

				print 'aqui'
				diretorio = os.listdir('/etc/')
				if 'script' not in diretorio:
					try:
						os.system('sudo mkdir /etc/script/')
						print '\n########################################################################'
						print '# Diretório criado com sucesso!                                        #'
								
						diretorio = os.listdir('/etc/')
						if 'script' in diretorio:
							try:
								os.system('cd $HOME/Downloads/del_captura_de_tela-master/ && sudo mv del_captura_de_tela.py /etc/script/')
								print '# Arquivo adicionado na pasta com sucesso! 	  		       #'

								diretorio_script = os.listdir('/etc/script/')
								if 'del_captura_de_tela.py' in diretorio_script:
									try:
										os.system('cd $HOME/Downloads/ && rm -r del_captura_de_tela-master/')
										print '# Arquivo atualizado ..                                                #'
										
										user = pasta.split('/')
										diretorio_etc = os.listdir("/etc/")
										comando = "*/1 * * * * "+user[2]+" python /etc/script/del_captura_de_tela.py"
										
										if 'crontab' in diretorio_etc:
											try:
												os.system("sudo cp /etc/crontab /etc/crontab-script")
												os.system("sudo cp /etc/crontab /etc/crontab-backup")
												os.system("sudo chmod 777 /etc/crontab-script")
												os.system("sudo chown diego:diego /etc/crontab-script")

												myfile = open('/etc/crontab-script', 'r+a')
												line = myfile.read()
												words = line.split("#")
												words = line.split("\n")

												if comando not in words:
													myfile.write("\n#Executa script de deletar screenshots.\n")
													myfile.write(comando+"\n")
													myfile.write("#\n")
													myfile.close()
													ok = True
													

												if ok:
													os.system("sudo cp /etc/crontab-script /etc/crontab")
													os.system("sudo rm /etc/crontab-script")
													os.system("sudo rm /etc/crontab-backup")
													print '# Crontab agendado no sistema com sucesso!                             #'
													print '# Instalação do script finalizada!                                     #'
													print '########################################################################'
												else:
													os.system("sudo cp /etc/crontab-backup /etc/crontab")
													os.system("sudo rm /etc/crontab-script")
													os.system("sudo rm /etc/crontab-backup")
													print '\nComando já agendado no sistema. Arquivo não atualizado!\n'

											except Exception, e:
												print 'Não foi possível agendar o arquivo no sistema!'
										
									except Exception, e:
										print 'Não foi possível deletar a pasta del_captura_de_tela-master/ em $HOME/Downloads'

								else:
									try:
										os.system('cd $HOME/Downloads/ && rm -r del_captura_de_tela-master/')
							
										user = pasta.split('/')
										diretorio_etc = os.listdir("/etc/")
										comando = "*/1 * * * * "+user[2]+" python /etc/script/del_captura_de_tela.py"
										
										if 'crontab' in diretorio_etc:
											try:
												os.system("sudo cp /etc/crontab /etc/crontab-script")
												os.system("sudo cp /etc/crontab /etc/crontab-backup")
												os.system("sudo chmod 777 /etc/crontab-script")
												os.system("sudo chown diego:diego /etc/crontab-script")

												myfile = open('/etc/crontab-script', 'r+a')
												line = myfile.read()
												words = line.split("#")
												words = line.split("\n")

												if comando not in words:
													myfile.write("\n#Executa script de deletar screenshots.\n")
													myfile.write(comando+"\n")
													myfile.write("#\n")
													myfile.close()
													ok = True
													

												if ok:
													os.system("sudo cp /etc/crontab-script /etc/crontab")
													os.system("sudo rm /etc/crontab-script")
													os.system("sudo rm /etc/crontab-backup")
													print 'Crontab agendado no sistema com sucesso!'
													print '\nInstalação do script com sucesso!'
												else:
													os.system("sudo cp /etc/crontab-backup /etc/crontab")
													os.system("sudo rm /etc/crontab-script")
													os.system("sudo rm /etc/crontab-backup")
													print '\nComando já agendado no sistema. Arquivo não atualizado!\n'

											except Exception, e:
												print 'Não foi possível agendar o arquivo no sistema!'

									except Exception, e:
										pass


							except Exception, e:
								pass#print 'Não foi possível mover o arquivo da pasta $HOME/Downloads/del_captura_de_tela-master/ '
						else:
							pass
							#print 'Arquivo del não existe ema /etc/script/'
					except Exception, e:
						print 'Não foi possível criar a pasta script/ em /etc/'
				else:
					print '\n########################################################################'
					print '# Diretório já criado, atualizando arquivos..                          #'
					diretorio_script = os.listdir('/etc/script/')
					if 'del_captura_de_tela.py' in diretorio_script:
						try:
							os.system('cd $HOME/Downloads/del_captura_de_tela-master/ && sudo mv del_captura_de_tela.py /etc/script/')
							print '# Arquivo atualizado com sucesso! 	  		               #'
							print '# Verificando Crontab .. 	  		                       #'

							os.system('cd $HOME/Downloads/ && rm -r del_captura_de_tela-master/')
							
							user = pasta.split('/')
							diretorio_etc = os.listdir("/etc/")
							comando = "*/1 * * * * "+user[2]+" python /etc/script/del_captura_de_tela.py"
									
							if 'crontab' in diretorio_etc:
								try:
									os.system("sudo cp /etc/crontab /etc/crontab-script")
									os.system("sudo cp /etc/crontab /etc/crontab-backup")
									os.system("sudo chmod 777 /etc/crontab-script")
									os.system("sudo chown diego:diego /etc/crontab-script")

									myfile = open('/etc/crontab-script', 'r+a')
									line = myfile.read()
									words = line.split("#")
									words = line.split("\n")

									if comando not in words:
										myfile.write("\n#Executa script de deletar screenshots.\n")
										myfile.write(comando+"\n")
										myfile.write("#\n")
										myfile.close()
										ok = True
									else:
										print '# Comando já agendado no sistema!    	  	                       #'
										print '########################################################################'


									if ok:
										os.system("sudo cp /etc/crontab-script /etc/crontab")
										os.system("sudo rm /etc/crontab-script")
										os.system("sudo rm /etc/crontab-backup")
										print 'Crontab agendado no sistema com sucesso!'
										print '\nInstalação do script com sucesso!'
									else:
										os.system("sudo cp /etc/crontab-backup /etc/crontab")
										os.system("sudo rm /etc/crontab-script")
										os.system("sudo rm /etc/crontab-backup")
										print '\nComando já agendado no sistema. Arquivo não atualizado!\n'

								except Exception, e:
									pass#print 'Não foi possível agendar o arquivo no sistema!'

						except Exception, e:
							pass
							#print 'Não foi possível deletar a pasta del_captura_de_tela-master/ em $HOME/Downloads'
							
			except Exception, e:
				print 'Não foi possível descompactar o arquivo.'

		else:
			print 'Arquivo del_captura_de_tela-master.zip não existe em $HOME/Downloads/'

	print '\n--> Lembre-se de compartilhar esse arquivo com alguem que tem o mesmo problema. (:'
	print "--> Em breve será feito melhorias neste arquivo, fiquem ligados. Enjoy!\n"

except Exception, e:
	print 'Falha crítica! Informe o criador do script ou algum programador que possa resolver.'
