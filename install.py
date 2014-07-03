#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess

try:
	pasta = os.environ["HOME"]
	user = pasta.split('/')
	
	download = os.listdir(pasta+"/Downloads/")
	print '################################################################################'
	print '# Iniciando instalação do script                                               #'
	print '################################################################################\n'
	#'

	if 'del_captura_de_tela-master' not in download:
		if 'del_captura_de_tela-master.zip' in download:
			try:
				os.system("cd $HOME/Downloads/ && unzip del_captura_de_tela-master.zip")

				diretorio = os.listdir('/etc/')
				if 'script' not in diretorio:
					try:
						os.system('sudo mkdir /etc/script/')
						print '\n################################################################################'
						print '# Diretório criado com sucesso!                                                #'

						diretorio = os.listdir('/etc/')
						if 'script' in diretorio:
							try:
								os.system('cd $HOME/Downloads/del_captura_de_tela-master/ && sudo mv del_captura_de_tela.py /etc/script/')
								print '# Arquivo adicionado na pasta com sucesso! 	  		                #'

								diretorio_script = os.listdir('/etc/script/')
								if 'del_captura_de_tela.py' in diretorio_script:
									try:
										os.system('cd $HOME/Downloads/ && rm -r del_captura_de_tela-master/')
										print '# Arquivo atualizado ..                                                        #'
										print '# Agendando arquivo no sistema ..                                              #'

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
													print '# Crontab agendado no sistema com sucesso!                                     #'
													print '# Instalação do script finalizada!                                             #'
													print '################################################################################'
												else:
													os.system("sudo cp /etc/crontab-backup /etc/crontab")
													os.system("sudo rm /etc/crontab-script")
													os.system("sudo rm /etc/crontab-backup")
													print '# Comando já agendado no sistema. Arquivo não atualizado!         #'

											except Exception, e:
												print '# Não foi preciso agendar o arquivo no sistema.                                #'
												print '# Comando já agendado! Arquivo crontab não atualizado.                         #'
												print '################################################################################'

									except Exception, e:
										print 'Não foi possível deletar a pasta del_captura_de_tela-master/ em $HOME/Downloads'

							except Exception, e:
								pass#print 'Não foi possível mover o arquivo da pasta $HOME/Downloads/del_captura_de_tela-master/ '

					except Exception, e:
						print 'Não foi possível criar a pasta script/ em /etc/'
				else:
					print '\n################################################################################'
					print '# Diretório já criado, atualizando arquivos..                                  #'
					diretorio_script = os.listdir('/etc/script/')
					if 'del_captura_de_tela.py' not in diretorio_script:
						try:
							os.system('cd $HOME/Downloads/del_captura_de_tela-master/ && sudo mv del_captura_de_tela.py /etc/script/')
							os.system('cd $HOME/Downloads/ && rm -r del_captura_de_tela-master/')
							print '# Verificando Crontab .. 	  		                               #'

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
										print '# Comando já agendado no sistema!    	  	                               #'

										if ok:
											os.system("sudo cp /etc/crontab-script /etc/crontab")
											os.system("sudo rm /etc/crontab-script")
											os.system("sudo rm /etc/crontab-backup")
											print 'Crontab agendado no sistema com sucesso!'
										else:
											os.system("sudo cp /etc/crontab-backup /etc/crontab")
											os.system("sudo rm /etc/crontab-script")
											os.system("sudo rm /etc/crontab-backup")
											print '# Comando já agendado no sistema. Arquivo não atualizado!         #'

								except Exception, e:
									print '# Não foi preciso agendar o arquivo no sistema!                                #'
									print '# Favor, altere-o manualmente.                      		               #'
									print '################################################################################'

						except Exception, e:
							pass
							#print 'Não foi possível deletar a pasta del_captura_de_tela-master/ em $HOME/Downloads'
					else:
						diretorio = os.listdir('/etc/')
						diretorio_script = os.listdir('/etc/script/')

						if 'script' in diretorio and 'del_captura_de_tela.py' in diretorio_script:
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
										print '# Comando já agendado no sistema!    	  	                               #'

									if ok:
										os.system("sudo cp /etc/crontab-script /etc/crontab")
										os.system("sudo rm /etc/crontab-script")
										os.system("sudo rm /etc/crontab-backup")
										print '# Crontab agendado no sistema com sucesso!                                     #'
										print '# Instalação do script finalizada!                                             #'
										print '################################################################################'
									else:
										os.system("sudo cp /etc/crontab-backup /etc/crontab")
										os.system("sudo rm /etc/crontab-script")
										os.system("sudo rm /etc/crontab-backup")
										print '# Comando já agendado no sistema. Arquivo não atualizado!         #'

								except Exception, e:
									print '# Não foi preciso agendar o arquivo no sistema!                                #'
									print '# Favor, altere-o manualmente.                      		               #'
									print '################################################################################'
							else:
								pass
			except Exception, e:
				print 'Não foi possível descompactar o arquivo.'

		else:
			print '# Arquivo del_captura_de_tela-master.zip não existe em $HOME/Downloads/        #'
			print '################################################################################'
	else:
		diretorio = os.listdir('/etc/')
		if 'script' not in diretorio:
			try:
				if 'script' not in diretorio:
					try:
						os.system('sudo mkdir /etc/script/')
						print '\n################################################################################'
						print '# Diretório criado com sucesso!                                                #'

						diretorio = os.listdir('/etc/')
						if 'script' in diretorio:
							try:
								os.system('cd $HOME/Downloads/del_captura_de_tela-master/ && sudo mv del_captura_de_tela.py /etc/script/')
								print '# Arquivo adicionado na pasta com sucesso! 	  		               #'

								diretorio_script = os.listdir('/etc/script/')
								if 'del_captura_de_tela.py' in diretorio_script:
									try:
										os.system('cd $HOME/Downloads/ && rm -r del_captura_de_tela-master/')
										print '# Arquivo atualizado ..                                                        #'
										print '# Agendando arquivo no sistema ..                                              #'

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
													print '# Crontab agendado no sistema com sucesso!                                     #'
													print '# Instalação do script finalizada!                                             #'
													print '################################################################################'
												else:
													os.system("sudo cp /etc/crontab-backup /etc/crontab")
													os.system("sudo rm /etc/crontab-script")
													os.system("sudo rm /etc/crontab-backup")
													print '# Comando já agendado no sistema. Arquivo não atualizado!         #'

											except Exception, e:
												print '# Não foi preciso agendar o arquivo no sistema.                                #'
												print '# Comando já agendado! Arquivo crontab não atualizado.                         #'
												print '################################################################################'

									except Exception, e:
										print 'Não foi possível deletar a pasta del_captura_de_tela-master/ em $HOME/Downloads'

							except Exception, e:
								pass#print 'Não foi possível mover o arquivo da pasta $HOME/Downloads/del_captura_de_tela-master/ '

					except Exception, e:
						pass#print 'Não foi possível criar a pasta script/ em /etc/'

			except Exception, e:
				pass

		else:
			try:
				print '\n################################################################################'
				print '# Diretório criado com sucesso!                                                #'
				diretorio = os.listdir('/etc/')
				diretorio_script = os.listdir('/etc/script/')
				if 'script' in diretorio and 'del_captura_de_tela.py' in diretorio_script:
					try:
						os.system('cd $HOME/Downloads/del_captura_de_tela-master/ && sudo mv del_captura_de_tela.py /etc/script/')
						print '# Arquivo atualizado com sucesso! 	  		                        #'

						diretorio_script = os.listdir('/etc/script/')
						if 'del_captura_de_tela.py' in diretorio_script:
							try:
								os.system('cd $HOME/Downloads/ && rm -r del_captura_de_tela-master/')
								print '# Arquivo atualizado ..                                                        #'
								print '# Agendando arquivo no sistema ..                                              #'

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
											print '# Comando já agendado no sistema!    	  	                               #'

										if ok:
											os.system("sudo cp /etc/crontab-script /etc/crontab")
											os.system("sudo rm /etc/crontab-script")
											os.system("sudo rm /etc/crontab-backup")
											print '# Crontab agendado no sistema com sucesso!                                     #'
											print '# Instalação do script finalizada!                                             #'
											print '################################################################################'
										else:
											os.system("sudo cp /etc/crontab-backup /etc/crontab")
											os.system("sudo rm /etc/crontab-script")
											os.system("sudo rm /etc/crontab-backup")
											print '# Comando já agendado no sistema. Arquivo não atualizado!         #'

									except Exception, e:
										print '# Não foi preciso agendar o arquivo no sistema.                                #'
										print '# Comando já agendado! Arquivo crontab não atualizado.                         #'
										print '################################################################################'

							except Exception, e:
								print 'Não foi possível deletar a pasta del_captura_de_tela-master/ em $HOME/Downloads'

					except Exception, e:
						pass#print 'Não foi possível mover o arquivo da pasta $HOME/Downloads/del_captura_de_tela-master/ '
				else:
					diretorio_script = os.listdir('/etc/script/')
					if 'del_captura_de_tela.py' not in diretorio_script:
						try:
							os.system('cd $HOME/Downloads/del_captura_de_tela-master/ && sudo mv del_captura_de_tela.py /etc/script/')
							os.system('cd $HOME/Downloads/ && rm -r del_captura_de_tela-master/')
							print '# Arquivo atualizado com sucesso! 	  		                       #'
							print '# Verificando Crontab .. 	  		                               #'

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
										print '# Comando já agendado no sistema!    	  	                               #'

									if ok:
										os.system("sudo cp /etc/crontab-script /etc/crontab")
										os.system("sudo rm /etc/crontab-script")
										os.system("sudo rm /etc/crontab-backup")
										print 'Crontab agendado no sistema com sucesso!'
									else:
										os.system("sudo cp /etc/crontab-backup /etc/crontab")
										os.system("sudo rm /etc/crontab-script")
										os.system("sudo rm /etc/crontab-backup")
										print '# Comando já agendado no sistema. Arquivo não atualizado!         #'

								except Exception, e:
									print '# Não foi preciso agendar o arquivo no sistema!                                #'
									print '# Favor, altere-o manualmente.                      		               #'
									print '################################################################################'

						except Exception, e:
							pass
							#print 'Não foi possível deletar a pasta del_captura_de_tela-master/ em $HOME/Downloads'


			except Exception, e:
				pass #EXISTE A PASTA JÁ DESZIPADA NO DOWNLOADS
	os.system('rm del_captura_de_tela-master.zip')
	print '\n################################################################################'
	print '# Lembre-se de compartilhar esse arquivo com alguem que tem o mesmo problema.  #'
	print "# Em breve será feito melhorias neste arquivo, fiquem ligados. Enjoy! (:       #"
	print '################################################################################\n'
	print '################################################################################'
	print '# Fim da instalação do script                                                  #'
	print '################################################################################\n'

except Exception, e:
	print 'Falha crítica! Informe o criador do script ou algum programador que possa resolver.'




