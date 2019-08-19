# URY
![Custom badge](https://img.shields.io/badge/version-2.0-orange)
![GitHub license](https://img.shields.io/badge/license-MIT-blue)
![Custom badge](https://img.shields.io/badge/python-3.6-green)
![Custom badge](https://img.shields.io/badge/scrapy-1.7.3-yellow)

URI Online Judge scrapy

## Screenshot
![Screenshot](Screenshot.png)

## Setup
Instalando as dependências.
```shell script
$ pip3 install scrapy
```

## Conceitos básicos
|     Comando     |    Descrição   |
|-----------------|----------------|
| -a start=NUMERO | Numero inicial |
| -a stop=NUMERO  | Numero final   |

Meios para salvar o resultado:

|        Comando        |                Descrição                |
|-----------------------|-----------------------------------------|
| -a path=CAMINHO       | Exportar para varios templates Python   |
| -o CAMINHO/DO/ARQUIVO | Exportar para um arquivo JSON, CSV, ... |

## Exemplos
Exportar para um template Python do 1005 até o 1010
```shell script
$ scrapy crawl problems -a path=DIRETORIO -a start=1005 -a stop=1010
```

Exportar para um arquivo JSON, usando o modo padrão (1001 até o 1005)
```shell script
$ scrapy crawl problems -o CAMINHO/DO/ARQUIVO 
```

## Licença
>Você pode verificar a licença completa [aqui](LICENSE)

Este projeto está licenciado sob os termos da licença ** MIT **.