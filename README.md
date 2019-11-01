# TPA
Trabalho de análise e benchmark de algoritmos de ordenação

## arquivos de dados
Os arquivos de dados devem ser colocados no diretório `src/input` no formato CSV e com o seguinte abeçalo

|email | gender | uid | birthdate | height | weight |
|:------:|:------:|:------:|:------:|:------:|:------:|

## para executar basta ter o Python 3 intalado

usando o comando 
```shell
$ python3 ./src/main.py --a <algoritmo> --input <arquivo.csv> --output <arquivo.csv> --times <numero>
``` 
é executado o projeto, a baixo os parametros são descritos.

-  `--a` 
    - seleciona os algoritmos
opções de algoritmos são:
`all, insertion, heap, merge, quick, selection, tim, intro`
 > a opção`all` lê todos os arquivos no diretório *input*
- `--times`
    - numero que diz quantas vezes irá rodar o mesmo algoritmo (opcional)
- `--input`
    - nome do arquivo de entrada csv com o formato descrito anteriormente
- `--output`
    - nome do arquivo de saida
    
## benchmark

Os dados do benchmark irão ser salvos em um arquivo chamado `records.dat` que está no diretório output.
