# WormVirus
Um repositório para guardar os passos e ideias que tivemos para fazer um vírus/malware, que ao estar escondido em um programa executável, se conecta com o computador no qual está hospedado o servidor e percorre todas as pastas do usuário em que está, em busca do arquivo alvo.
Projeto desenvolvido para o segundo semestre de 2020 (2020/2) do HackoonSpace.

:warning: ***AVISO IMPORTANTE! Esse repositório serve apenas para propósitos educacionais: não use para uso malicioso, não tomaremos responsabilidade por atos ilícitos. Este conteúdo só está disponibilizado para aprendizado e pesquisa.*** :warning:

## Conceito do Projeto:
O Projeto foi desenvolvido como um teste para observar as capacidades que um "vírus caseiro" tem de penetrar nos arquivos e diretórios de um computador. Para fazer o projeto, pensamos em incorporar o vírus como um executável, que seria baixado por um usuário qualquer da internet. Para ilustrar os casos nos quais isso ocorre, o vírus foi inserido em uma versão "crackeada" do jogo Among Us, algo que alguém possivelmente baixaria um arquivo zip ou rar e rodaria o executável sem conferir todas as pastas no arquivo baixado.
Sendo um vírus de ação direta, a proposta do vírus é simples: Receber informações sobre a localização e a provedora de internet do usuário e executar uma série de comandos em seu computador (a partir da biblioteca OS do python), quando o jogo for executado, a partir de um arquivo batch (.bat) rodando minimizado na pasta /Users . A partir desses comandos, a ideia seria procurar por diversos arquivos importantes baseados em seus tipos (txt, json, etc.) e enviar uma cópia deles para o computador do servidor. No entanto, para tornar o programa menos perigoso para testes, ele apenas procura por um txt específico no computador do usuário, nomeado por `flagHackoon.txt`. Ao ser encontrado, o conteúdo do arquivo é copiado para um txt no servidor, nomeado pelo IP do cliente.

## Pré-requisitos e recursos utilizados:

A programação foi feita 100% em python, mas como o arquivo foi transformado em um executável, na teoria não seria necessário ter Python instalado. no entanto, como o programa não foi testado em computadores sem python, pode ser necessário ter uma versão do python 3, recomendamos que seja a mais recente.

## Passo a passo:

1. Estudamos e aprendemos sobre as seguintes bibliotecas e aplicações do **python**:
```
import socket
import os
import sys
import glob
import random
```

2. Construímos 2 scripts de python: 1 para o lado do cliente e outro para o lado do servidor. Os conteúdos de cada script serão disponibilizados nas imagens ao fim do repositório.

3. Os comandos possíveis de se usar em Windows para a cópia e transferência do conteúdo de arquivos foram estudados pelo site oficial da Microsoft[1].

4. O programa foi convertido para um executável usando a biblioteca `pyinstaller`[2].
## Instalação:

Após instalar o python, usando o GitHub pelo seu browser, clique no botão verde "Code" e em "Download ZIP". Após a conclusão do download, extraia a pasta para a sua área de trabalho.

## Execução:



## Bugs/problemas conhecidos:

Por enquanto não há nenhum bug visual ou de sintaxe no programa, mas qualquer problema com o programa basta mandar uma mensagem por email ou pelo discord/whatsapp do [HackoonSpace](https://hackoonspace.com) caso faça parte, ou para o GitHub de algum dos autores do projeto.

## Autores:

* Caio César Brandini da Silva ([caiobrandini](https://github.com/caiobrandini))
* Fernando Favareto Abromovick ([kyleflick124](https://github.com/kyleflick124))
* Vinícius Carvalho Venturini ([Vinicius-Venturini](https://github.com/Vinicius-Venturini))

## Demais anotações e referências:
[1] https://docs.microsoft.com/pt-br/windows-server/administration/windows-commands/windows-commands

[2] https://pyinstaller.readthedocs.io/en/stable/usage.html

## Imagens e Screenshots do programa:



