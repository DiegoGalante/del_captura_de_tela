LEIA-ME
===================

Deleta ScreenShot(s) acidentai(s) para usuário de alguns modelos de notebook da Dell. Apenas testado e funcionando por enquanto no Ubuntu 14.04.

Arquivo responsável por verificar e deletar o(s) ScreenShoot(s) contido na pasta $HOME/Imagens/ 

#INSTRUÇÕES DE USO:
- Faça o download do arquivo, abra o temrinal (CTRL + ALT + T) e digite o seguinte comando:

        cd $HOME/Downloads && unzip del_captura_de_tela-master.zip && cd $HOME/Downloads

- Para instalar os arquivos basta utilizar o comando:

        python $HOME/Downloads/del_captura_de_tela-master/install.py


#OBSERVAÇÕES IMPORTANTES: 
- Este arquivo foi testado e aprovado somente em Ubuntu 14.04.
- A utilização em qualquer outro sistema operacional é de total responsabilidade de quem fizer.
- Apenas funciona (até o momento) para linguagem PT-BR, ou seja, o PrintScreen necessariamente precisa ter o seguinte nome: "Captura de tela de ..... 13:27:14" ou "Captura de tela de ..... 13:27:14 - ".

#IMPORTANTE!
- Caso quiser realmente capturar uma tela, renomeie a imagem logo em seguida de capturá-la pois corre o risco de esquecer e o processo deletar a mesma.
