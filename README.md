# PORTSCANNER

  Software simples feito em python que serve como um scaner de portas usando o protocolo TCP/IP, foi usada a biblioteca Socket para realizar conexões e envios de pacotes   através dos protocolos mencionados. Em seguida usa a biblioteca Colorama para ajudar na identificação de portas Abertas e portas Fechadas, por último, utiliza-se a biblioteca Time e Datetime para manipulação do tempo.
<div align=center><img src="https://github.com/cvinicius369/PortScanner/assets/137227050/e74396f7-3a68-4db6-acc7-3c151196771e"></div>

## Funcionamento
### Preparação - Definilção de portas e alvo:
   
  É feito um banner (simples) para testar o funcionamento da biblioteca colorama, em seguida é criado um array "ports" que irá conter as portas que serão testadas, feito isso uma variavel irá armazenar o ip ou link do alvo, por exemplo "localhost".
<div align=center><img src="https://github.com/cvinicius369/PortScanner/assets/137227050/8853aa49-4ea4-440a-9d41-41aca681f8ce"></div>

### Teste de Portas
A partir da função For, são testadas cada porta dentro do array, onde dentro da função for é criado um socket TCP/IP que pode ser usado para se conectar a outros computadores usando o protocolo IPv4, espera-se 0.5 segundos e tenta uma conexão (ou envio de pacote) com o alvo na porta especificiada. Caso o "code" retorne 0, a porta está aberta então imprimirá a mensagem em verde de "Porta Aberta", caso contrário, vermelho informando "Porta fechada", em ambos os casos também é informado código de retorno.
<div align=center><img src="https://github.com/cvinicius369/PortScanner/assets/137227050/fdb27b1b-3503-48d2-897f-08d605d045e6"></div>

## Menu

É criado um menu para testar a execução do portscanner, caso ocorra tudo corretamente o código será iniciado.
<div align=center><img src="https://github.com/cvinicius369/PortScanner/assets/137227050/6a5266d7-9f93-40ce-8f44-cab9da410caa"></div>

#OBS
Este código é apenas para fins educacionais, use com moderação.


