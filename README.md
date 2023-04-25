# Web Scraping em Python

Este é um projeto em Python que utiliza as bibliotecas `requests`, `BeautifulSoup` e `selenium` para realizar web scraping de um site de passagens aéreas.

## Requisitos

- Python 3.x
- Bibliotecas `requests`, `BeautifulSoup` e `selenium`
- Driver do Chrome (ou outro navegador de sua escolha) para selenium

## Como usar

1. Clone este repositório
2. Instale as bibliotecas necessárias (`requests`, `BeautifulSoup` e `selenium`)
3. Instale o driver do navegador que deseja usar com o selenium
4. Execute o arquivo `webscraping.py` em um terminal
5. Siga as instruções para fornecer os detalhes do voo desejado

## Como funciona

Este projeto utiliza web scraping para acessar o site de passagens aéreas da Smiles, preencher os detalhes do voo fornecidos pelo usuário e coletar informações sobre as opções de voo disponíveis. O script usa `requests` e `BeautifulSoup` para fazer a primeira conexão com o site e coletar as informações iniciais de sessão. Em seguida, usa o `selenium` para preencher o formulário de busca e coletar as informações de voo.

## Limitações

Este script é específico para o site da Smiles e foi projetado para funcionar com as especificações atuais do site.
O site pode ser atualizado ou alterado a qualquer momento, o que pode fazer com que este script pare de funcionar. 
O código é fornecido apenas para fins educacionais e não deve ser usado para raspar dados sem permissão.
