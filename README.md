del_captura_de_tela
===================

Deleta ScreenShot(s) acidentai(s) para usuário de alguns modelos de notebook da Dell. Apenas testado e funcionando por enquanto no Ubuntu 14.04.

Arquivo responsável por verificar e deletar o(s) ScreenShoot(s) contido na pasta $HOME/Imagens/ 

OBSERVAÇÕES: 
- Este arquivo foi testado e aprovado somente em Ubuntu 14.04. A utilização em qualquer outro sistema operacional é de total responsabilidade de quem fizer.
- Apenas funciona (até o momento) para linguagem PT-BR, ou seja, o PrintScreen necessariamente precisa ter o seguinte nome: "Captura de tela de ..... 13:27:14" ou "Captura de tela de ..... 13:27:14 - ".

INSTRUÇÕES DE USO:
- Para adicionar a pasta no local adequado digite o segundo comando no terminal:

    sudo mkdir /etc/script/

-Entre no diretório que está o arquivo "del_captura_de_tela.py", e o envie para a pasta script:

    sudo mv del_captura_de_tela.py /etc/script/

- Verifique se os arquivos estão no local corretamente:

    cd /etc/script/
    ls
    del_captura_de_tela.py

AGENDANDO A TAREFA NO SISTEMA(crontab):
- Para agendar esse script no sistema, utilize o seguinte comando no terminal:

    crontab -e

- Direcione o cursor até a ultima linha e adicione exatamente o seguinte comando:

    */1 * * * * python /etc/script/del_captura_de_tela.py

    #OBS: O "*/1" indica a quantidade de tempo em que será processado o arquivo. Ou seja, de um em um minuto será verificado e executado o processo na pasta.

- Reinicialize a cron:
    
    sudo service cron restart
