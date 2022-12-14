# Constans

## tipos
os tipos de unidade de medida podem ser adicionados com uma certa facilidade, basta seguir algumas regras:

1. Crie o arquivo que vai receber as proporções `tempo.txt`.
2. Dentro dele siga o seguinte modelo: `nome,símbolo, p, q`
    1. nome: nome da medida
    2. símbolo: abreviação da unidade
    3. "p" e "q" são inteiros cuja fração "p/q" representa o multiplicador de tal unidade
3. É necessário escolher uma unidade referência para todas as outras, e, nela, "p" = "q" = 1
4. Obrigatoriamente todos os nomes de unidades devem começar com letra maiúscula e outras palavras devem começar com letra minúscula
5. segue um exemplo com unidades temporais:
```
Minuto,min,1,1
Segundo,s,60,1
Hora,h,1,60
Dia,dia,1,1440
Semana,sem,1,10080
```
Note que :
- A unidade de referência é "minuto" e não necessariamente é a de menor valor.
- Sabemos que há 60 segundos em um minuto, logo "p/q" de segundos = 60/1 pois, ao converter x minutos para segundos, multiplicamos x por 60, ou seja, fazemos **x*(p/q)**.
- Todas as unidades começam com letra maiúscula mas, o nome do arquivo deve ser com letra minuscula.


## Considerações finais
- Terminadas essas etapas, basta adicionar, em **letras minúsculas**, o nome do novo tipo que você acabou de adicionar para que ele apareça na lista.
- Por padrão, as unidades de *potências de base 10* que multiplicam as unidades, devem aparecer para todas as unidades e automaticamente é selecionada a *potência 0*.
- Caso alguma coisa funcione fora do esperado, compare seu arquivo com os demais já presentes nesse aplicativo.